
//   let textarea = document.querySelectorAll("textarea");
//   let lines = [];
//   let currentLine = 0;

//   textarea.addEventListener("keydown", function(event) {
//     if (event.key === "Enter") {
//       lines[currentLine] = textarea.value.substring(0, textarea.selectionStart);
//       currentLine++;
//       textarea.value = "";
//       for (let i = 0; i < currentLine; i++) {
//         textarea.value += (i + 1) + ". " + lines[i] + "\n";
//       }
//       event.preventDefault();
//     }
//   });


function displayInput() {
    var input = document.getElementById("inputField").value;
    var addHtml="<ol><li>" + input + "<i class='fa-solid fa-trash-check'> </i>"+ "</li></ol>"
    document.getElementById("displayDiv").innerHTML = addHtml;
  }
