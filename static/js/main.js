const name = []
const id =[]

const advice_title = []
const investigation_name = []

function getCookie(name) {
    // Split cookie string and get all individual name=value pairs in an array
    var cookieArr = document.cookie.split(";");

    // Loop through the array elements
    for(var i = 0; i < cookieArr.length; i++) {
        var cookiePair = cookieArr[i].split("=");

        /* Removing whitespace at the beginning of the cookie name
        and compare it with the given string */
        if(name == cookiePair[0].trim()) {
            // Decode the cookie value and return
            return decodeURIComponent(cookiePair[1]);
        }
    }

    // Return null if not found
    return null;
}




let medicineAdd = document.getElementById("medicine-add")
let prescriptionView = document.getElementById("prescription-view")

const medicines =[]
const advices =[]
if(medicineAdd) {
    medicineAdd.addEventListener("click",(e)=>{
        e.preventDefault();
        let medicine = document.getElementById("medicine").value;
        let medicineDose = document.getElementById("medicine-dose").value;
        let medicineInstruction = document.getElementById("medicine-instruction").value;
        let medicineDuration = document.getElementById("medicine-duration").value;
        let index = name.indexOf(medicine);

        document.getElementById("medicine").value = "";
        document.getElementById("medicine-dose").innerHTML = document.getElementById("medicine-dose").innerHTML;
        document.getElementById("medicine-instruction").innerHTML=document.getElementById("medicine-instruction").innerHTML;
        document.getElementById("medicine-duration").innerHTML=document.getElementById("medicine-duration").innerHTML;

        fetch(`http://127.0.0.1:8000/api/add-medicine/`,{
                method:'POST',
                headers:{
                    'Content-Type':'application/json',
                    "X-CSRFToken": getCookie("csrftoken")
                },
                body:JSON.stringify({'medicine':id[index],"dose":medicineDose,'instruction':medicineInstruction,'duration':medicineDuration})

                })
                .then(response => response.json())
                .then(data =>{
                    table=document.getElementById("table-body")
                    table.innerHTML += `<tr class="single-medcine"> <td>${data['medicine']['name']}</td> <td>${data['dose']}</td> <td>${data['instruction']}</td><td>${data['duration']}</td></tr>`
                    medicines.push(data)
                })
    })

}

if(prescriptionView){
    prescriptionView.addEventListener("click",(e)=>{
        e.preventDefault()
        console.log(medicines)
        let name = document.getElementById("patient-name").value
        let age = document.getElementById("patient-age").value
        let phone = document.getElementById("patient-phone").value
        let advice = document.getElementsByClassName("advice")

        for(let i=0;i<advice.length;i++){
            advices.push(advice[i].value)
        }
        const prescription_data = {
            patient_name:name,
            patient_age:age,
            patient_phone:phone,
            advice:advices,

        };

        console.log(prescription_data)

    })
}

// function autocomplete(inp, arr) {
//   /*the autocomplete function takes two arguments,
//   the text field element and an array of possible autocompleted values:*/
//   var currentFocus;
//   /*execute a function when someone writes in the text field:*/
//   inp.addEventListener("input", function(e) {
//       var a, b, i, val = this.value;
//       /*close any already open lists of autocompleted values*/
//       closeAllLists();
//       if (!val) { return false;}
//       currentFocus = -1;
//       /*create a DIV element that will contain the items (values):*/
//       a = document.createElement("DIV");
//       a.setAttribute("id", this.id + "autocomplete-list");
//       a.setAttribute("class", "autocomplete-items");
//       /*append the DIV element as a child of the autocomplete container:*/
//       this.parentNode.appendChild(a);
//       /*for each item in the array...*/
//       for (i = 0; i < arr.length; i++) {
//         /*check if the item starts with the same letters as the text field value:*/
//         if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
//           /*create a DIV element for each matching element:*/
//           b = document.createElement("DIV");
//           /*make the matching letters bold:*/
//           b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
//           b.innerHTML += arr[i].substr(val.length);
//           /*insert a input field that will hold the current array item's value:*/
//           b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
//           /*execute a function when someone clicks on the item value (DIV element):*/
//               b.addEventListener("click", function(e) {
//               /*insert the value for the autocomplete text field:*/
//               inp.value = this.getElementsByTagName("input")[0].value;
//               /*close the list of autocompleted values,
//               (or any other open lists of autocompleted values:*/
//               closeAllLists();
//           });
//           a.appendChild(b);
//         }
//       }
//   });
//   /*execute a function presses a key on the keyboard:*/
//   inp.addEventListener("keydown", function(e) {
//       var x = document.getElementById(this.id + "autocomplete-list");
//       if (x) x = x.getElementsByTagName("div");
//       if (e.keyCode == 40) {
//         /*If the arrow DOWN key is pressed,
//         increase the currentFocus variable:*/
//         currentFocus++;
//         /*and and make the current item more visible:*/
//         addActive(x);
//       } else if (e.keyCode == 38) { //up
//         /*If the arrow UP key is pressed,
//         decrease the currentFocus variable:*/
//         currentFocus--;
//         /*and and make the current item more visible:*/
//         addActive(x);
//       } else if (e.keyCode == 13) {
//         /*If the ENTER key is pressed, prevent the form from being submitted,*/
//         e.preventDefault();
//         if (currentFocus > -1) {
//           /*and simulate a click on the "active" item:*/
//           if (x) x[currentFocus].click();
//         }
//       }
//   });
//   function addActive(x) {
//     /*a function to classify an item as "active":*/
//     if (!x) return false;
//     /*start by removing the "active" class on all items:*/
//     removeActive(x);
//     if (currentFocus >= x.length) currentFocus = 0;
//     if (currentFocus < 0) currentFocus = (x.length - 1);
//     /*add class "autocomplete-active":*/
//     x[currentFocus].classList.add("autocomplete-active");
//   }
//   function removeActive(x) {
//     /*a function to remove the "active" class from all autocomplete items:*/
//     for (var i = 0; i < x.length; i++) {
//       x[i].classList.remove("autocomplete-active");
//     }
//   }
//   function closeAllLists(elmnt) {
//     /*close all autocomplete lists in the document,
//     except the one passed as an argument:*/
//     var x = document.getElementsByClassName("autocomplete-items");
//     for (var i = 0; i < x.length; i++) {
//       if (elmnt != x[i] && elmnt != inp) {
//       x[i].parentNode.removeChild(x[i]);
//     }
//   }
// }
// /*execute a function when someone clicks in the document:*/
// document.addEventListener("click", function (e) {
//     closeAllLists(e.target);
// });
// }




function get_medicine(){
    let response =  fetch(`http://127.0.0.1:8000/api/medicine-list/`,{
                method:'GET',
                headers:{
                    'Content-Type':'application/json',
                },
                })
                .then(response => response.json())
                .then(data =>{
                    medicineName(data)
                })

}
function medicineName(medicineset){

    for(let i=0; medicineset.length>i; i++) {
        let data = medicineset[i]
        name.push(data['name'])
        id.push(data['id'])
    }

}

function get_advice(){
    let response =  fetch(`http://127.0.0.1:8000/api/advice-list/`,{
                method:'GET',
                headers:{
                    'Content-Type':'application/json',
                },
                })
                .then(response => response.json())
                .then(data =>{
                    adviceTitle(data)
                })
}

function adviceTitle(adviceset){

    for(let i=0; adviceset.length>i; i++) {
        let data = adviceset[i]
        advice_title.push(data['title'])
    }

}


function get_investigation(){
    let response =  fetch(`http://127.0.0.1:8000/api/investigation-list/`,{
                method:'GET',
                headers:{
                    'Content-Type':'application/json',
                },
                })
                .then(response => response.json())
                .then(data =>{
                    investigationName(data)
                })
}

function investigationName(investigationSet){

    for(let i=0; investigationSet.length>i; i++) {
        let data = investigationSet[i]
        investigation_name.push(data['name'])
    }

}


get_medicine()
get_advice()
get_investigation()


  $( function() {

    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }

    $( "#investigation" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            investigation_name, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });


    $( "#advice" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            advice_title, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });

    $( "#medicine" ).autocomplete({
      source: name
    });

  } );









