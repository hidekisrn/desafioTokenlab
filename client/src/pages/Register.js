import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function Register(){

    const [values, setValues] = useState({
        username: '',
        password: ''
    });

    const register = event => {
        fetch('http://localhost:8000/api/register/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(values)
        })
        .catch(error => console.log('error:', error))
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
            <Link to='/'>
                <button onClick={register}>Registrar</button>
            </Link>
        </div>
    )
}

export default Register;