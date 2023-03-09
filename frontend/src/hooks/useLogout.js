import React from "react";
import { Logout } from "../services/Logout";
import useAuth from "./useAuth";

const useLogout = () => {
  const { setAuth } = useAuth();
  return Logout(setAuth);
};

export default useLogout;
