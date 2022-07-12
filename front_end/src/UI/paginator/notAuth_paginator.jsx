import React from 'react';
import { Link } from 'react-router-dom';
import Mybutton from '../buttons/MyButton';

const NotAuthPaginator = ({ page, changePage }) => {

    let barItems = [
        {id:1, title:'Home', to:'/home', addTitle:'home'},
        {id:2, title:'Registration', to:'/registration',addTitle:'Registration'},
        {id:3, title:'Login', to:'/login',addTitle:'Login'},
        
    ]
    return (
        <div>
            <div className='navbar__header'>
            {barItems.map(p =>
                    <Link onClick={() => changePage(p)} key={p.id} className={window.location.pathname===p.to 
                        ? ' header__link_get header__link'
                        : 'header__link'  } to={p.to}><strong>{p.title}</strong>
                    </Link>
                    
            )}
            </div>

        </div>
    );
}

export default NotAuthPaginator;