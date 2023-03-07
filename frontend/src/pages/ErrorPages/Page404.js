import React from 'react';
import { Box, Button,Typography } from '@mui/material';
import ThemeLight from '../../components/Theme/ThemeLight'
import { createMuiTheme} from '@mui/material';
import CssBaseline from "@mui/material/CssBaseline";
import {ThemeProvider } from "@mui/material/styles";

//can add a photo of somesort like most 404 pages
export default function Page404() {
    document.title = "404 Page Not Found";
    let themeLight = createMuiTheme(ThemeLight);
    return(
        <ThemeProvider theme={themeLight}>
        <Box sx = {{display: 'flex', justifyContent: 'center', alignItems: 'center', flexDirection:'column', minHeight: '100vh'}}>
            <CssBaseline />
            <Typography variant='h1'>
                404
            </Typography>
            <Typography variant='h5'color="gray">
                The page you're looking for doesn't exist.
            </Typography>
            {/**Currently links to signin page, but it should go back to home */}
            {/**Linked using href instead of Router atm */}
            <Button href="/signin" type="create" id="bottom-create" variant="contained" sx={{mt:3, mb:2, color: 'white', ':hover':{ bgcolor: '#6fb8e1'}}} color="retyrn_blue">
            Return
          </Button>
        </Box>
        </ThemeProvider>
    );
}