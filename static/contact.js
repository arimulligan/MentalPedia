// (A) SEND CONTACT FORM
function send () {
    // (A1) PREVENT MULTIPLE SUBMIT
    document.getElementById("contactGo").disabled = true;
  
    // (A2) COLLECT FORM DATA
    let data = new FormData(document.getElementById("contactForm"));
  
    // (A3) SEND!
    fetch("/send", { method:"POST", body:data })
    .then(res => {
        if (res.status==200) { location.href = "/thankyou"; }
        else {
        console.log(res);
        alert("Opps an error has occured.");
    }
    })
    .catch(err => {
        console.error(err);
        alert("Opps an error has occured.");
    });
    return false;
}