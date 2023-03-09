import * as React from "react";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import {ThemeProvider } from "@mui/material/styles";
import ThemeLight from '../../components/Theme/ThemeLight'
import { createMuiTheme, Card } from '@mui/material';


export default function SignUp() {
  document.title = "Create Company";
  let themeLight = createMuiTheme(ThemeLight);
  return (
    <ThemeProvider theme={themeLight}>
      <Grid container spacing={0} direction="column" alignItems="center" justify="center" style={{ minHeight: '100vh' }}>
      <Card sx={{marginTop:10, width: 850, maxWidth: 900, maxHeight: 700, borderRadius: 3, boxShadow: 2, display: 'flex', alignItems: 'center' }}>
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
          <Box component="form" sx={{ mt: 3, width: 800 }}>
            <Grid container spacing={2}>
              <Grid item xs={12}>
                <TextField
                  autoComplete="company-name"
                  name="companyName"
                  required
                  fullWidth
                  id="companyName"
                  label="Company Name"
                  autoFocus
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="Owner Name"
                  label="Owner Name"
                  name="OwnerName"
                  autoComplete="owner-name"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="company-email"
                  label="Email Address"
                  name="CompanyEmail"
                  autoComplete="company-email"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="company-address"
                  label="Company Address"
                  name="company address"
                  autoComplete="company-address"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="company-phone"
                  label="Company Phone Number"
                  name="company phone"
                  autoComplete="company-phone"
                />
              </Grid>
            </Grid>
          </Box>
        </Box>
        <Box component="span" m={0} display="flex" justifyContent="space-between" alignItems="center"sx={{marginBottom: 12}}>
          {/**Button links to nothing yet, should go back to previous page */}
          <Button component={Link} to="/" type="cancel" id="bottom-create" variant="contained" sx={{mt:3, mb:2, color: 'white', ':hover':{ bgcolor: '#c9c7c7'}}} color="cancel_color">
            Cancel
          </Button>
          {/**Button links to nothing yet, should go to new company "wallet/display" */}
          <Button component={Link} to="/" type="create" id="bottom-create" variant="contained" sx={{mt:3, mb:2, color: 'white', ':hover':{ bgcolor: '#6fb8e1'}}} color="retyrn_blue">
            Create
          </Button>
        </Box>
      </Container>
      </Card>
      </Grid>
    </ThemeProvider>
  );
}
