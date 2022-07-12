import axios from "axios";
import React from "react";
import { useEffect } from "react";
import { useState } from "react";
import WorkerItem from "../components/workerItem";
import Mybutton from "../UI/buttons/MyButton";

const WorkerList = () => {
  useEffect(() => {
    getWorker();
  }, []);

  const [workers, setWorkers] = useState([]);
  const getWorker = async () => {
    const res = await axios.get("http://127.0.0.1:8000/api/client/workerList/");
    setWorkers(res.data);


    console.log(res);
  };

  return (
    <div className="group__wrapper">
      {workers.map((worker) => (
        <WorkerItem worker={worker} />
      ))}
    </div>
  );
};

export default WorkerList;
