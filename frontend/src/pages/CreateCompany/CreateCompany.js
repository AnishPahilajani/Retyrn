import TextField from "@mui/material/TextField";
import Grid from "@mui/material/Grid";
import React from "react";
const initialValues = {
  companyType: "",
  companyName: "",
};
const CreateCompany = () => {
  return (
    <Grid container columns={{ xs: 4, sm: 8, md: 12 }}>
      <Grid item xs={4}>
        <TextField required id="outlined-required" label="Type of Company" />
      </Grid>
      <Grid item xs={4}>
        <TextField
          required
          id="outlined-required"
          label="Company Name"
          defaultValue="Hello World"
        />
      </Grid>
      <Grid item xs={4}>
        <TextField
          required
          id="outlined-required"
          label="Company Address"
          defaultValue="Hello World"
        />
      </Grid>
      <Grid item xs={4}>
        <TextField
          required
          id="outlined-required"
          label="Company Phone Number"
          defaultValue="Hello World"
        />
      </Grid>
      <Grid item xs={4}>
        <TextField
          required
          id="outlined-required"
          label="Owner Name"
          defaultValue="Hello World"
        />
      </Grid>
    </Grid>
  );
};

export default CreateCompany;
