import React, { useEffect, useState } from "react";
// import SignUpForm from "../../components/Client/Login/SignUpForm";
import { useAuth } from "../../hooks/useAuth";
import { useNavigate } from "react-router-dom";
import LoginModal from "./login_modal";
import LoginCSS from "./login.module.css"

const Login = () => {
    const { isCorrect, useRegister, useLogin, useSocialLogin } = useAuth();
    const handleClose = () => setShow(false);
    const [id, setId] = useState(null);
    const [show, setShow] = useState(true);
    const form_type = 'login';
    const navigate = useNavigate();

    useEffect(() => {
        if (isCorrect) {
            navigate('/home');
        }
    }, [isCorrect, navigate]);

    useEffect(() => {
    // setShow(true);
    // console.log(show);
    }, []);


    const emit_register = (userData) => {
            useRegister(userData);
    }

    const emit_login = (userdata) => {
            useLogin(userdata);
    }

    const emit_sociallogin = (userdata) => {
            useSocialLogin(userdata);
        // console.log(userdata);
    }


    return (
        <>
            <div className={LoginCSS.background}>
                <LoginModal form_type={form_type} show={show} onAddUser={emit_register} onLoginUser={emit_login} SocialLogin={emit_sociallogin} handleClose={handleClose} />
            </div>        
        </>
    )
}

export default Login;