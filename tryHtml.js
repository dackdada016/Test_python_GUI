var fileName = [];
var errorContainer = null;
var successContainer = null;

function useState(initialValue) {
  var state = initialValue;

  function setState(newState) {
    state = newState;
    render();
  }

  return [state, setState];
}

function useEffect(effectFunction, dependencies) {
  var hasMounted = false;
  var previousDependencies = [];

  function checkDependencies() {
    var dependenciesChanged = dependencies.some(function(dep, index) {
      return dep !== previousDependencies[index];
    });

    if (!hasMounted || dependenciesChanged) {
      effectFunction();
      previousDependencies = dependencies;
    }
  }

  checkDependencies();
  hasMounted = true;
}

function handleFileChange(event) {
  const files = Array.from(event.target.files);
  const names = files.map((file) => file.name);
  setFileName(names);
    if (files.length === 1) {
    // 取得選擇的單一檔案
    const file = files[0];
    console.log(file);
    } else {
      console.log(files);
    }
}

function setFileName(names) {
  fileName = names;
  render();
}

function render() {
  var fileNameContainer = document.getElementById("fileNameContainer");
  fileNameContainer.innerHTML = "";
  fileName.forEach(function(name) {
    var span = document.createElement("span");
    span.innerText = name;
    fileNameContainer.appendChild(span);
    var br = document.createElement("br");
    fileNameContainer.appendChild(br);
  });
}

function displayError() {
  if (!errorContainer) {
    errorContainer = document.createElement("h3");
    errorContainer.innerText = "傳輸錯誤";
    errorContainer.style.color = "red";
    var button = document.querySelector(".btn-primary");
    button.parentNode.insertBefore(errorContainer, button.nextSibling);
  }
}

// function displaySuccess() {
  // if (!successContainer) {
    // successContainer = document.createElement("h3");
    // successContainer.innerText = "傳輸成功";
    // successContainer.style.color = "green";
    // var form = document.getElementById("uploadTextFile");
    // form.innerHTML = "";
    // var newForm = document.createElement("form");
    // newForm.id = "uploadExcel";
    // newForm.name = "uploadExcel";
    // var uploadFileDiv = document.createElement("div");
    // uploadFileDiv.className = "upload-file";
    // var label = document.createElement("label");
    // label.className = "icon-area";
    // var input = document.createElement("input");
    // input.type = "file";
    // input.accept = ".xlsx";
    // input.multiple = "multiple";
    // input.id = "uploadExcel";
    // label.appendChild(input);
    // uploadFileDiv.appendChild(label);
    // newForm.appendChild(uploadFileDiv);
    // form.parentNode.insertBefore(newForm, form.nextSibling);
    // var newFileNameContainer = document.createElement("div");
    // newFileNameContainer.className = "mb-5";
    // newFileNameContainer.id = "fileNameContainer";
    // newForm.parentNode.insertBefore(newFileNameContainer, newForm.nextSibling);
    // var newButton = document.createElement("button");
    // newButton.type = "button";
    // newButton.className = "btn btn-primary";
    // newButton.innerText = "分析";
    // newForm.parentNode.insertBefore(newButton, newForm.nextSibling);
    // var newFileInput = document.getElementById("uploadExcel");
    // newFileInput.addEventListener("change", handleFileChange);
  // }
// }

window.onload = function() {
  var fileInput = document.getElementById("fileInput");
  fileInput.addEventListener("change", handleFileChange);
  render();

  var nextButton = document.querySelector(".btn-primary");
  nextButton.addEventListener("click", function(event) {
    event.preventDefault();
    var formData = new FormData(document.querySelector("#uploadTextFile"));
    var files = fileInput.files;
    console.log(formData.values);
    for (var i = 0; i < files.length; i++) {
      formData.append("file", files[i]);
    }

    fetch("http://127.0.0.1:5050/uploadtxt/", {
      method: "POST",
      body: formData
    })
      .then(function(response) {
        if (response) {
          // POST OK
          console.log(response);
          // displaySuccess();
        } else {
          // POST Error
          displayError();
          console.log("POST ERROR");
        }
      })
      .catch(function(error) {
        console.error("Error:", error);
      });
  });
};
