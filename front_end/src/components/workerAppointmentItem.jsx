import { observer } from "mobx-react-lite";
import { useState } from "react";
import {Link, useParams} from "react-router-dom"
import $api from "../http";
import Mybutton from "../UI/buttons/MyButton";
import Mydeletebtn from "../UI/buttons/MydeleteButton";
import Mymodal from "../UI/modal/myModal";

const WorkerAppointmentItem = ({appointment}) => {



  return (
    <div className="group__wrapper">
        {appointment.map((app) => (
    <div className="post">
        
    <div className="post__content">
    <div key={Date.now()} className="groups">
        <div className="post__body"><strong>Date:</strong> {app.date}</div>
        <div className="post__body"><strong>apointment_start:</strong> {app.apointment_start}</div>
        <div className="post__body"><strong>apointment_end:</strong> {app.apointment_end}</div>
        <div className="post__body"><strong>apointment_worker:</strong> {app.user}</div>
    </div>
      
</div>
</div>
))} 
</div>
  );
};

export default observer(WorkerAppointmentItem);