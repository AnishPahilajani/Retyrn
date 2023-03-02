import * as React from 'react';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Link from '@mui/material/Link';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Checkbox, CssBaseline, FormControlLabel, TextField } from '@mui/material';

const { palette } = createTheme();
const { augmentColor } = palette;
const createColor = (mainColor) => augmentColor({ color: { main: mainColor } });

const themeLight = createTheme({
    
    palette: {
        retyrn_blue: createColor('#4ca7da'),
        background: {
            default: "#fafafa"
        }
    }
});

export default function SignIn() {
    document.title = "Sign in";
    return(
        <ThemeProvider theme={themeLight}>
        <Container component="main" maxWidth="xs">
            <CssBaseline/>
            <Box sx={{ marginTop:20, display:'flex', flexDirection:'column', alignItems:'center'}}>
                    <Typography component="h1"variant="h4"> {/** Page Name fields */}
                        Sign In
                    </Typography>
                    <Box component="form"> {/** Form fields */}
                        <TextField required fullWidth id="email" label="Email Address" name="email" margin="normal" autoComplete="email" autoFocus/>
                        <TextField required fullWidth id="password" label="Password" name="password" type="password" margin="normal" autoComplete="current-password"/>
                        <FormControlLabel control={<Checkbox value="remember" color="retyrn_blue"/>} label="Remember me"/>
                        <Button type="submit" fullWidth variant="contained" sx={{mt:3, mb:2, color: 'white', ':hover':{ bgcolor: '#6fb8e1'}}} color="retyrn_blue">Sign In</Button>
                        <Grid container>
                            <Grid item xs>
                                <Link href="#" variant="body2">
                                    Forgot password?
                                </Link>
                            </Grid>
                            <Grid item>
                                <Link href="/signup" variant="body2">
                                    Don't have an account? Sign Up
                                </Link>
                            </Grid>
                        </Grid>
                    </Box>
            </Box>
        </Container>
        </ThemeProvider>
    );
}