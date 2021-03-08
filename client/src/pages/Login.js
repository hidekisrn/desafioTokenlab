import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function Login(){

    const [values, setValues] = useState({
        username: '',
        password: ''
    });

    const login = event => {
        fetch('http://localhost:8000/api/auth/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(values)
        })
        .then( data => data.json())
        .then(
            data =>{
                console.log('data:', data.token);
            }
        ).catch(error => console.log('error:', error))
        console.log('logado');
        console.log('credentials:', values);
    };

    const onChange = (event) => {
        setValues({ ...values, [event.target.name]: event.target.value});
    };



    return(
        <div>
            <p>Login</p>

            <label>
                Username:
                <input type="text" name="username" value={values.username} onChange={onChange}/>
            </label>
            <br/>
            <label>
                Password:
                <input type="password" name="password" value={values.password} onChange={onChange}/>
            </label>
            <br/>
            <button onClick={login}>Entrar</button>
            <Link to='/register'>
                <button>Registrar</button>
            </Link>
        </div>
    )
}

export default Login;