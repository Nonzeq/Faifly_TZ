import React from 'react';
import { Link } from 'react-router-dom';
import Store from '../../store/store';
import Mybutton from '../buttons/MyButton';

const Paginator = ({ page, changePage, role }) => {

    
        let barItems = [
            {id:1, title:'Home', to:'/home', addTitle:'home'},
            // {id:2, title:'Worker List', to:'/workerList',addTitle:'Worker list'},
            // {id:3, title:'My Appointment', to:'/userAppointment',addTitle:'My Appointment'},
            // // {id:4, title:'Login', to:'/login',addTitle:'Login'},
            
        ]
        if(localStorage.getItem('role')==='CUSTOMER'){
            barItems.push({id:2, title:'Worker List', to:'/workerList',addTitle:'Worker list'},)
            barItems.push({id:3, title:'My Appointment', to:'/userAppointment',addTitle:'My Appointment'},)
        }else{
            barItems.push({id:3, title:'Appointment', to:'/workerAppointment',addTitle:'Appointment'},)
        }
        


    return (
        <div>
            
            {barItems.map(p =>
                    <Link onClick={() => changePage(p)} key={p.id} className={window.location.pathname===p.to 
                        ? ' header__link_get header__link'
                        : 'header__link'  } to={p.to}><strong>{p.title}</strong>
                    </Link>,
                   
                    
            )}
            
            </div>

        
    );
}

export default Paginator;