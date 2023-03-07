import React from "react";
import useAuth from "../hooks/useAuth";
const Dashboard = () => {
  const { auth } = useAuth();
  console.log(auth);
  return <div>Dashboard</div>;
};

export default Dashboard;
