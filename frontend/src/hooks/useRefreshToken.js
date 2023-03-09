import useAuth from "./useAuth";
import { RefreshToken } from "../services/RefreshToken";
const useRefreshToken = () => {
  const { setAuth } = useAuth();
  return RefreshToken(setAuth);
};

export default useRefreshToken;
