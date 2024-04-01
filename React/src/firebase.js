import { initializeApp } from 'firebase/app';
import { getAuth, GoogleAuthProvider } from 'firebase/auth';


const firebaseConfig = {
    apiKey: "AIzaSyDAU23NmOC7mAIZ0HvFyEbXvYEjNWiJ93I",
    authDomain: "tfg-kikogilabert.firebaseapp.com",
    projectId: "tfg-kikogilabert",
    storageBucket: "tfg-kikogilabert.appspot.com",
    messagingSenderId: "686855205701",
    appId: "1:686855205701:web:9b0f6248cc21da056a442c"
  };

    // Initialize Firebase
    export const app = initializeApp(firebaseConfig);
    export const auth = getAuth();
    export const googleProvider = new GoogleAuthProvider();