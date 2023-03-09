
export default function ComingSoon() {
    document.title = "Coming Soon";
    let themeLight = createMuiTheme(ThemeLight);
    return(
        <ThemeProvider theme={themeLight}>
        <Box sx = {{display: 'flex', justifyContent: 'center', alignItems: 'center', flexDirection:'column', minHeight: '100vh'}}>
            <CssBaseline />
            <Typography variant='h3' fontFamily={'roboto'} color="#4ca7da" style={{ lineHeight: "100px" }}>
                Coming Soon!
            </Typography>
            <Typography variant='h5'color="gray" fontFamily={'roboto'}>
                The page you're looking for is currently under production.
            </Typography>
            <Typography variant='h5'color="gray" fontFamily={'roboto'}>
                Come back another time!
            </Typography>
            {/**Currently links to nothing, but it should go back to home */}
            {/**Linked using href instead of Router atm */}
            <Button href="/" type="return" id="bottom-return" variant="contained" sx={{mt:5, mb:2, color: 'white', ':hover':{ bgcolor: '#6fb8e1'}}} color="retyrn_blue">
                Return
            </Button>
        </Box>
        </ThemeProvider>
    );
}