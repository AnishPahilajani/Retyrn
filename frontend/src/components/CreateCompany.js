import * as React from "react";
import { useEffect } from "react";
import { UseForm } from "../hooks/useForm";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { createTheme, ThemeProvider } from "@mui/material/styles";

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

const theme = createTheme();
const initialValues = {
  company_name: "",
  owner_name: "",
  company_email: "",
  company_address: "",
  company_phone: "",
};
export default function SignUp() {
  document.title = "Create Company";
  const { values, setValues, handleInputChange } = UseForm(initialValues);
  useEffect(() => {
    console.log(values);
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
          <Typography component="h1" variant="h4">
            Create Company
          </Typography>
          <Box component="form" sx={{ mt: 3 }}>
            <Grid container spacing={2}>
              <Grid item xs={12}>
                <TextField
                  onChange={handleInputChange}
                  autoComplete="company-name"
                  name="company_name"
                  required
                  fullWidth
                  id="companyName"
                  label="Company Name"
                  autoFocus
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  onChange={handleInputChange}
                  required
                  fullWidth
                  id="Owner Name"
                  label="Owner Name"
                  name="owner_name"
                  autoComplete="owner-name"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  onChange={handleInputChange}
                  required
                  fullWidth
                  id="company-email"
                  label="Email Address"
                  name="company_email"
                  autoComplete="company-email"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  onChange={handleInputChange}
                  required
                  fullWidth
                  id="company-address"
                  label="Company Address"
                  name="company_address"
                  autoComplete="company-address"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  onChange={handleInputChange}
                  required
                  fullWidth
                  id="company-phone"
                  label="Company Phone Number"
                  name="company_phone"
                  autoComplete="company-phone"
                />
              </Grid>
            </Grid>
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
              Create
            </Button>
          </Box>
        </Box>
      </Container>
    </ThemeProvider>
  );
}
