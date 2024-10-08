

function
    $("#image-picker").change(function (event) {
        readURL(this);
        document.getElementById('error').style.display = 'none';
    
    });
        function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            pushImage(input.files[0])
    
            reader.onload = function (e) {
                $('#image-preview').attr('src', e.target.result);
            }
    
            reader.readAsDataURL(input.files[0]);
    
    
        }
        }

    
    var firebaseLink = document.getElementById("firebaseLink").innerText
    // Push batch images to storage and store references in the database
    var pushImage = function (file) {
        document.getElementById('submitButton').innerHTML = `
        <button class="pill-button-alternate" style=" width=100%"><i class="fa fa-pause-circle-o" aria-hidden="true" style="color:'white'"></i>Please wait while we upload your image</button>
        `

        // var uid = firebase.auth().currentUser.uid;
        // Create storage reference
        var ref = firebase.storage().ref(`/ineruu-142dc-default-rtdb/Images/`).child(file.name + ".jpg");
    
        // Upload file and get task
        var task = ref.put(file, {contentType: file.type});
    
        // Monitor task for progress
        task.on('state_changed',
            // Shows progress of task
            function progress(snapshot) {
                var percentage = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
                console.log(percentage);
            },
            // Shows any errors occurring during progress
            function error(err) {
                // Handle unsuccessful uploads
                console.log(err.message);
    
            },
            // Shows when task is completed
            function complete() {
                // Handle successful uploads on complete
                var image = task.snapshot.downloadUrl;
                var secondImage = task.snapshot.ref.getDownloadURL().then(function(downloadURL) {
            console.log('File available at', downloadURL);
        //    firebaseLink = downloadURL
            document.getElementById("firebaseLink").value = downloadURL
        //    console.log("Firebase Link: " + firebaseLink)
            document.getElementById('submitButton').innerHTML = `{{form.submit (class="pill-button",onclick="showLoadingScreen()", style="width:100%")}}`

            });
    
                // Data model to be uploaded to the database
                var data = {
                    imageUrl: image
                };
                
            
            });  
    };
    
    
        function changeimagesss(event) {
        console.log(event)
        pushImage(event)
    
        
        }
