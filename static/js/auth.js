
  // Your web app's Firebase configuration


  const config = {
    apiKey: "AIzaSyDr7sOBMFAeNZHS5W34TEvma_IzmJ4Dz80",
    authDomain: "mybubblenet-326f3.firebaseapp.com",
    databaseURL: "https://mybubblenet-326f3.firebaseio.com",
    storageBucket: "mybubblenet-326f3.appspot.com",
    messagingSenderId: "495901667657",
  };
  // Initialize Firebase
  firebase.initializeApp(config);

  //firestore referencias
  // Get a reference to the storage service, which is used to create references in your storage bucket
  function uploadimage(){
  var storage = firebase.storage();
  var file = document.getElementById("file").files[0];
  var storageRef = storage.ref();
  var thisref = storageRef.child(file.name).put(file);
  thisref.on('state_changed',function(snapshot){
  console.log("file uplaoded succesfully");
  },
  function(error) {
  },
  function() {
  // Upload completed successfully, now we can get the download URL
  var downloadURL = thisref.snapshot.downloadURL;
  console.log("got url");
  document.getElementById("url").value = downloadURL;
  alert("file uploaded successfully");
});
    }
  //actulizacion firestore


