function radioButtonSelected(radioBtnName){
    var radioValue = document.getElementsByName(radioBtnName);

    for(i = 0; i < radioValue.length; i++) { 
        if(radioValue[i].checked) 
        return radioValue[i].value
    }    
    
}

function dropDownSelected(dropDownName){

    var ddValue = document.getElementById(dropDownName);

    for (var i = 0; i < ddValue.options.length; i++) {
        if (ddValue.options[i].selected) {
            return ddValue.options[i].value
        }
      }
}


function onClickedPredict(){

    // field values
    var age = document.getElementById("age").value
    console.log("age: "+age)
    // radio btn values
    var sex = radioButtonSelected("sex");
    console.log("Type of sex selected: "+sex)
    // drop down list
    var chestPain = dropDownSelected("cp");
    console.log("Type of chestPain selected: "+chestPain)
    // field values
    var trestbps = document.getElementById("trestbps").value
    console.log("trestbps: "+trestbps)
    // radio btn values
    var chol = radioButtonSelected("chol");
    console.log("Type of chol selected: "+chol)

    // field values
    var fbs = document.getElementById("fbs").value
    console.log("fbs: "+fbs)
    // radio btn values
    var restecg = radioButtonSelected("restecg");
    console.log("Type of restecg selected: "+restecg)

    var thalach = document.getElementById("thalach").value
    console.log("thalach: "+thalach)
    // radio btn values
    var exang = radioButtonSelected("exang");
    console.log("Type of exang selected: "+exang)

    var oldpeak = document.getElementById("oldpeak").value
    console.log("oldpeak: "+oldpeak)
    // radio btn values
    var slope = radioButtonSelected("slope");
    console.log("Type of slope selected: "+slope)

    // radio btn values
    var ca = radioButtonSelected("ca");
    console.log("Type of ca selected: "+ca)

    var thal = document.getElementById("thal").value
    console.log("thal: "+thal)


    user_data = {"age":parseInt(age), 
                "sex":parseInt(sex), 
                "cp":parseInt(chestPain), 
                "trestbps":parseInt(trestbps),
                "chol":parseInt(chol),
                "fbs":parseInt(fbs),
                "restecg":parseInt(restecg),
                "thalach":parseInt(thalach),
                "exang":parseInt(exang),
                "oldpeak":parseFloat(oldpeak),
                "slope":parseInt(slope),
                "ca":parseInt(ca),
                "thal":parseInt(thal)}



    var url = "http://127.0.0.1:5000/v1/model/predict"

     // POST
     fetch(url, {

        // Declare what type of data we're sending
        headers: {
        'Content-Type': 'application/json'
        },

        // Specify the method
        method: 'POST',

        // A JSON payload
        body: JSON.stringify(user_data)
    }).then(function (response) { // At this point, Flask has printed our JSON
        return response.json();
    }).then(function (json) {

        console.log('POST response: ');

        // Should be 'OK' if everything was successful
        console.log(json);
        var predictPrice = document.getElementById("clf_prediction");
        predictPrice.innerHTML = "<h4>Presence of heart disease: " + json.prediction + "</h4>";
    });  
}