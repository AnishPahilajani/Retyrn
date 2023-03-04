import * as React from "react";
import { UseForm } from "../../components/UseForm";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Link from "@mui/material/Link";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import ThemeLight from '../../components/Theme/ThemeLight'
import { createMuiTheme } from '@mui/material';
import {
  Checkbox,
  CssBaseline,
  FormControlLabel,
  TextField,
} from "@mui/material";

const initialValues = {
  email: "",
  password: "",
  rememberMe: false,
};
export default function SignIn() {
    document.title = "Sign in";
  let themeLight = createMuiTheme(ThemeLight);
  const { values, setValues, handleInputChange } = UseForm(initialValues);
  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log(values);
    try {
      let resp = await fetch("http://localhost:8000/users", {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(values),
      });
      let data = await resp.json();
    } catch (err) {
      console.log(err);
    }
  };
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
              type="email"
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
                <Link href="#" variant="body2">
                  Forgot password?
                </Link>
              </Grid>
              <Grid item>
                <Link href="/signup" variant="body2">
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
