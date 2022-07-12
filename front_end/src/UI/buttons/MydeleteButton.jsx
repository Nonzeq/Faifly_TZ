
import React from 'react';
import classes from './MyDeleteBtn.module.css';
const Mydeletebtn = ({ children, ...props }) => {
    return (
        <button{...props} className={classes.myDeleteBtn}>
            <strong>{children}</strong>
        </button>
    );
}

export default Mydeletebtn;