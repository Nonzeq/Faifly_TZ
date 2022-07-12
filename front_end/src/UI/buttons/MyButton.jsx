import React from 'react';
import classes from './MyButton.module.css';

const Mybutton = ({ children, ...props }) => {
    return (
        <button{...props} className={classes.myBtn}>
            <strong>{children}</strong>
        </button>
    );
}

export default Mybutton;