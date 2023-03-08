import { createTheme} from '@mui/material/styles';

const { palette } = createTheme();
const { augmentColor } = palette;
const createColor = (mainColor) => augmentColor({ color: { main: mainColor } });

const ThemeLight = {
    
    palette: {
        retyrn_blue: createColor('#4ca7da'),
        cancel_color: createColor('#b3b1b1'),
        background: {
            default: "#fafafa"
        }
    }
};

export default ThemeLight;
