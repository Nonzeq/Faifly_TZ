import { observer } from "mobx-react-lite";
import { useState } from "react";
import {Link, useParams} from "react-router-dom"
import Mybutton from "../UI/buttons/MyButton";
const WorkerItem = (props) => {


  return (
    <div key={props.worker.id} className="post">
      <div className="post__content">
        <div key={Date.now()} className="groups">
          <strong>ID: {props.worker.id}</strong>
          <div className="post__body">
          <Link to={`/workers/${props.worker.id}`}><Mybutton>{props.worker.full_name}</Mybutton></Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default observer(WorkerItem);
