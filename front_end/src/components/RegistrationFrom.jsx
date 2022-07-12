import React from 'react';
import { useContext } from 'react';
import { useState } from 'react';
import { Context } from '..';
import Mybutton from '../UI/buttons/MyButton';
import Myinput from '../UI/inputs/MyInput';
import { observer } from "mobx-react-lite";
import { Link } from 'react-router-dom';
import axios from 'axios';
import $api from '../http';




const RegistrationForm = () => {
    const[username, setUsername] = useState('')
    const[email, setEmail] = useState('')
    const[password, setPassword] = useState('')
    const[password2, setPassword2] = useState('')
    const[role, setRole] = useState('')
    const[error, setError] = useState(null)
    const {store} = useContext(Context)
    const roles = [
        {id:1, title:'CUSTOMER'},
        {id:2, title:'WORKER'}
    ]

    // const registration = async() =>{
    //     const res = await $api.post('http://127.0.0.1:8000/auth/register/',{
    //         withCredentials:true,
    //         username:username,
    //         email:email,
    //         password:password,
    //         password2:password2,
    //         role:role,
    //     }).then(res => (console.log(res))).catch(e => setError(e.response.data))
        
    //     if(res.status == 201){
    //       setError('')
    //     }
    // }


    return ( 
<div>
{error && <div style={{color:'red'}}>{error.date || error[0]}</div>}
                <Myinput 
                onChange={e => setUsername(e.target.value)}
                value={username}
                type='text'
                placeholder='username'
            />
            <Myinput 
                onChange={e => setEmail(e.target.value)}
                value={email}
                type='email'
                placeholder='Email'
            />
            <Myinput
                onChange={e => setPassword(e.target.value)}
                value={password}
                type='password'
                placeholder='Password'
            />
                        <Myinput
                onChange={e => setPassword2(e.target.value)}
                value={password2}
                type='password'
                placeholder='Password2'
            />
            {/* <Myinput 
            onChange={e => setRole(e.target.value)}
            value={role}
            type='select'
            placeholder='role'
            /> */}
                <select style={{ margin: '20px 20px' }} value={role} onChange={e => setRole(e.target.value )}>
                <option key={roles.id}>Take your role</option>
                {roles.map((p) => <option key={p.id} value={p.title}>{p.title}</option>)}
            </select>
           <Mybutton onClick={() => store.registration(username, email, password,password2,role)}>Register</Mybutton>
</div>
     );
}
 
export default observer(RegistrationForm);