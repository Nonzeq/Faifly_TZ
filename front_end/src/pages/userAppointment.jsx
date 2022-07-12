import React, { useEffect, useState } from "react";
import UserAppointment_Item from "../components/userAppointment_Item";
import { useFetching } from "../hooks/useFetching";
import $api from "../http";
import Mybutton from "../UI/buttons/MyButton";
import Myloader from "../UI/Loader/ Myloader";

const UserAppointment = () => {
  useEffect(() => {
    getUserAppointment();
  }, []);
  const [appointment, setAppointment] = useState([]);

  const [getUserAppointment, isLoading, isErorr] = useFetching(async () => {
    try {
          const response = await $api.get(
            `http://127.0.0.1:8000/api/client/userAppointment/?user=${localStorage.getItem("id")}`
          );
          setAppointment(response.data);
        } catch (e) {
          console.log(e.response.data);
        }


  })

  // const getUserAppointment = async () => {
  //   try {
  //     const response = await $api.get(
  //       `http://127.0.0.1:8000/api/client/userAppointment/?user=${localStorage.getItem("id")}`
  //     );
  //     setAppointment(response.data);
  //   } catch (e) {
  //     console.log(e.response.data);
  //   }
  // };

  return (
    <div><div className="appointment__wrapper">  
        <h2>My Appointment</h2></div>
    <div className="appointment__wrapper">   
      {/* <div className="post">
        
        <div className="post__content">
            
          <div key={Date.now()} className="groups"> */}
            
            {/* {appointment.map((app) => (
              <p>
                <strong>Date: </strong>{app.date}|
                <strong>apointment_start: </strong>
                  {app.apointment_start} | 
                  <strong>apointment_end:</strong>
                  {app.apointment_end}|
                <strong>apointment_worker:</strong>
                {app.apointment_worker}

              </p>
            ))} */}
            {isLoading
            ?<div className='users'><div className="loaderError__container"><Myloader /></div></div>
            :<UserAppointment_Item appointment={appointment} />
}
          </div>
        </div>
    //   </div>
    // </div>
    // </div>
  );
};

export default UserAppointment;
