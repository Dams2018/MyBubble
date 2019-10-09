
  // Your web app's Firebase configuration
  var firebaseConfig = {
    apiKey: "AIzaSyDr7sOBMFAeNZHS5W34TEvma_IzmJ4Dz80",
    authDomain: "mybubblenet-326f3.firebaseapp.com",
    databaseURL: "https://mybubblenet-326f3.firebaseio.com",
    projectId: "mybubblenet-326f3",
    storageBucket: "",
    messagingSenderId: "495901667657",
    appId: "1:495901667657:web:2629d55863304ef9"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

  //firestore referencias
  const auth = firebase.auth();
  const db =firebase.firestore();

  //actulizacion firestore

