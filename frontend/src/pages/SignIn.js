import * as React from "react";
import { UseForm } from "../hooks/useForm";
import { useState, useEffect } from "react";
import { GetToken } from "../services/GetToken";
import useAuth from "../hooks/useAuth";
import { Link, useNavigate } from "react-router-dom";
import Typography from "@mui/material/Typography";
import Alert from "@mui/material/Alert";
import Container from "@mui/material/Container";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import Paper from "@mui/material/Paper";
import Box from "@mui/material/Box";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import {
  Checkbox,
  CssBaseline,
  FormControlLabel,
  TextField,
} from "@mui/material";

const { palette } = createTheme();
const { augmentColor } = palette;
const createColor = (mainColor) => augmentColor({ color: { main: mainColor } });
const themeLight = createTheme({
  palette: {
    retyrn_blue: createColor("#4ca7da"),
    background: {
      default: "#fafafa",
    },
  },
});
const initialValues = {
  email: "",
  password: "",
};
const SIGNIN_URL = "token/no-oauth";
export default function SignIn() {
  const { setAuth } = useAuth();
  const navigate = useNavigate();
  const { values, setValues, handleInputChange } = UseForm(initialValues);
  const [errMsg, setErrMsg] = useState("");
  const handleSubmit = (event) => {
    event.preventDefault();
    GetToken(SIGNIN_URL, values, setErrMsg, setAuth, navigate);
  };
  useEffect(() => {}, [errMsg]);
  useEffect(() => {
    setErrMsg("");
  }, [values]);
  return (
    <ThemeProvider theme={themeLight}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 20,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          {errMsg === "" ? <></> : <Alert severity="error">{errMsg}</Alert>}
          <Typography component="h1" variant="h4">
            Sign In
          </Typography>
          <Box component="form" onSubmit={handleSubmit}>
            <TextField
              onChange={handleInputChange}
              required
              fullWidth
              id="email"
              label="Email Address"
              name="email"
              margin="normal"
              autoComplete="email"
              autoFocus
            />
            <TextField
              onChange={handleInputChange}
              required
              fullWidth
              id="password"
              label="Password"
              name="password"
              type="password"
              margin="normal"
              autoComplete="current-password"
            />
            <FormControlLabel
              control={
                <Checkbox value={true} name="rememberMe" color="retyrn_blue" />
              }
              label="Remember me"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{
                mt: 3,
                mb: 2,
                color: "white",
                ":hover": { bgcolor: "#6fb8e1" },
              }}
              color="retyrn_blue"
            >
              Sign In
            </Button>
            <Grid container>
              <Grid item xs>
                <Link to="#" variant="body2">
                  Forgot password?
                </Link>
              </Grid>
              <Grid item>
                <Link to="/signup" variant="body2">
                  {"Don't have an account? Sign Up"}
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
      </Container>
    </ThemeProvider>
  );
}
