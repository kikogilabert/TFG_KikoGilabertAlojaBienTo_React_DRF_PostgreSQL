import React, { useState, useEffect, useCallback } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Modal from 'react-bootstrap/Modal';
import { useNavigate } from "react-router-dom";
import { GoogleReCaptchaProvider, GoogleReCaptcha } from "react-google-recaptcha-v3";
import Styles from './login.module.css';
import { getAuth, FacebookAuthProvider, signInWithPopup } from "firebase/auth";
import { auth, googleProvider } from '../../firebase';

function LoginModal({show, handleClose, onAddUser, onLoginUser, SocialLogin}){



    const [token, setToken] = useState("");
    const [refreshReCaptcha, setRefreshReCaptcha] = useState(false);
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();
    const [form_type, setForm_type] = useState('login');
    
    const signInGoogle = () => {
      signInWithPopup(auth, googleProvider)
            .then((result) => {
              console.log(result.user);
              let user = {
                username: result.user.displayName,
                email: result.user.email,
                password: result.user.uid,
                is_google_user: true
              };
              SocialLogin(user);
            })
            .catch((error) => {
              console.log(error);
            }); 
      };


  const handleSubmit = (e) => {
        e.preventDefault();
        try{
          if(form_type === 'login'){
            const userdata = { username, password };
            onLoginUser(userdata);
        }else{
            const newuserdata = { username, email, password };
            onAddUser(newuserdata);
        }
        }catch(e){
          setRefreshReCaptcha(!refreshReCaptcha);
          console.log(e);
        }
     
  };


  const handleRedirect = () => {
    if(form_type === 'register'){
      setForm_type('login');
      navigate('/login');
    }else{
      setForm_type('register');
      navigate('/login');
    }
  };

  const handleUsernameNameChange = (e) => {
    setUsername(e.target.value);
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const onVerify = useCallback((token) => {
    setToken(token);
  }, []);

  // const setTokenFunc = (getToken) => {
  //   // console.log(getToken);
  //   setToken(getToken);
  // };

  return (
        <>
      <Modal show={show} onHide={handleClose} form_type={form_type}
        backdrop="static"
        keyboard={true}>
        <Modal.Header closeButton>
        {form_type === 'login' && (
          <Modal.Title>Log In</Modal.Title>
        )}
        {form_type === 'register' && (
          <Modal.Title>Register</Modal.Title>
        )}
        </Modal.Header>
        <Modal.Body>
          <Form>
            {form_type === 'login' && (
              <Form.Group className="mb-3" controlId="login">
                <Form.Label>Username</Form.Label>
                <Form.Control  value={username}  type="text" placeholder='' onChange={handleUsernameNameChange}
                autoFocus />

                <Form.Label>Password</Form.Label>
                <Form.Control value={password} type="password" placeholder='' onChange={handlePasswordChange}/>

              </Form.Group>
            )}
            {form_type === 'register' && (
              <Form.Group className="mb-3" controlId="register">
                <Form.Label>Username</Form.Label>
                  <Form.Control value={username} type="text"  onChange={handleUsernameNameChange}/>
                
                <Form.Label>Email</Form.Label>
                  <Form.Control value={email} type="email" onChange={handleEmailChange} />
                
                <Form.Label>Password</Form.Label>
                  <Form.Control value={password} type="password" onChange={handlePasswordChange} />
              </Form.Group>
            )}
          <GoogleReCaptchaProvider reCaptchaKey={import.meta.env.VITE_RECAPTCHA_API_KEY}>
          <GoogleReCaptcha
            className={Styles.recaptcha}
            onVerify={onVerify}
            refreshReCaptcha={refreshReCaptcha}
          />
        </GoogleReCaptchaProvider>
          </Form>
          {/* Social Login */}
          <div className={Styles.slogin_icons}>
          <img onClick={signInGoogle} width={55} height={55} src="https://static-00.iconduck.com/assets.00/google-icon-2048x2048-czn3g8x8.png" />
          </div>
    
        </Modal.Body>
      <Modal.Footer>
      {form_type === 'login' && (
        <a onClick={handleRedirect} className='mb-3'>No account? Register now</a>
      )}
      {form_type === 'register' && (
        <a onClick={handleRedirect} className='mb-3'>Already have an account?</a>
      )}
        <Button variant="secondary" onClick={handleClose}>
          Close
        </Button>
        <Button variant="primary" onClick={handleSubmit}>
          {form_type === 'login' && (
            <span>Log In</span>
          )}
          {form_type === 'register' && (
            <span>Register</span>
          )}
        </Button>
      </Modal.Footer>
    </Modal>
    </>
  );
}

export default LoginModal;