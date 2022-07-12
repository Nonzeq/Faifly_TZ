import { observer } from "mobx-react-lite";
import { useState } from "react";
import {Link, useParams} from "react-router-dom"
import $api from "../http";
import Mybutton from "../UI/buttons/MyButton";
import Mydeletebtn from "../UI/buttons/MydeleteButton";
import Mymodal from "../UI/modal/myModal";

const UserAppointmentItem = ({appointment}) => {


    const deleteUserAppointment = async (id) =>{
        // try{
        //     const response = $api.delete(`http://127.0.0.1:8000/api/client/DeleteAppointment/${id}/`)
        //     console.log(response);
        // }catch(e){
        //     console.log(e.response);}

        const res = await $api.delete(`http://127.0.0.1:8000/api/client/DeleteAppointment/${id}/`,{

      }).then(res => (res)).catch(e => console.log(e.response.data))
        if(res.status == 204){
            window.location.reload() 
        }
        
        // window.location.reload()     
    }
    const [modal, setModal] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
  return (
    <div>
        {appointment.map((app) => (
    <div className="post">
        
    <div className="post__content">
    
        <div className="post__body"><strong>Date:</strong> {app.date}</div>
        <div className="post__body"><strong>apointment_start:</strong> {app.apointment_start}</div>
        <div className="post__body"><strong>apointment_end:</strong> {app.apointment_end}</div>
        <div className="post__body"><strong>apointment_worker:</strong> {app.apointment_worker}</div>
    </div>
      
    <div className='btns'>
        {/* <Mybutton>Edit User</Mybutton> */}
        {/* <Mymodal visible={modal} setVisible={setModal}><Updateuser
            key={props.user.id}
            create={props.create}
            user={props.user}
            groups={props.groups}>
        </Updateuser></Mymodal> */}
        <Mymodal visible={modal} setVisible={setModal}>
            <h1>Delete this Appointment on date {app.date}?</h1>
<Mydeletebtn onClick={() => deleteUserAppointment(app.id)}  >Delete</Mydeletebtn>
        
        </Mymodal>
        <Mydeletebtn onClick={() => setModal(true)} >Delete Appointment</Mydeletebtn>
        {/* onClick={() => deleteUserAppointment(app.id)} */}
    </div>

</div>
))} 
</div>
  );
};

export default observer(UserAppointmentItem);