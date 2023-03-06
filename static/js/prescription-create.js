const medicine_name = []
const medicine_id =[]

const advice_title = []
const investigation_name = []

const medicines =[]
const advices =[]
const instructions =[]

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
        medicine_name.push(data['name']+" "+data['group']+" "+data['type'])
        medicine_id.push(data['id'])
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

console.log(medicine_name)
console.log(advice_title)
console.log(investigation_name)

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


    $( "#generalAdvice" )
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
      source: medicine_name
    });

  } );







function displayInput(prescription) {

        let medicine = document.getElementById("medicine").value;
        let medicineDose = document.getElementById("medicine-dose").value;
        let medicineInstruction = document.getElementById("medicine-instruction").value;
        let medicineDuration = document.getElementById("medicine-duration").value;
        let index = medicine_name.indexOf(medicine);

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
                body:JSON.stringify({'prescription':prescription,'medicine':medicine_id[index],"dose":medicineDose,'instruction':medicineInstruction,'duration':medicineDuration})

                })
                .then(response => response.json())
                .then(data =>{
                    let input = document.getElementById("addedMedicines");
                    let addHtml=`<li>${data['medicine']['name']} ${data['medicine']['group']} ${data['medicine']['type']} | ${data['dose']} | ${data['instruction']} | ${data['duration']}</li><br>`
                    input.innerHTML+=addHtml
                    medicines.push(data)
                })

  }




//   let prescriptionView = document.getElementById("prescription-view")
//

//
//
// if(prescriptionView){
//     prescriptionView.addEventListener("click",(e)=>{
//         e.preventDefault()
//         console.log(medicines)
//         let name = document.getElementById("patient-name").value
//         let age = document.getElementById("patient-age").value
//         let phone = document.getElementById("patient-phone").value
//         let advice = document.getElementsByClassName("advice")
//
//         for(let i=0;i<advice.length;i++){
//             advices.push(advice[i].value)
//         }
//         const prescription_data = {
//             patient_name:name,
//             patient_age:age,
//             patient_phone:phone,
//             advice:advices,
//
//         };
//
//         console.log(prescription_data)
//
//     })
// }
//












