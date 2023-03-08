import { useLocation, Navigate, Outlet } from "react-router-dom";
import useAuth from "../hooks/useAuth";

const RequireAuth = ({ allowedRoles }) => {
  const { auth } = useAuth();
  const location = useLocation();

  return auth?.accessToken ? (
    <Outlet />
  ) : (
    <div>
      {console.log(auth.accessToken)}
      <Navigate to="/signin" state={{ from: location }} replace />
    </div>
  );
};

export default RequireAuth;
