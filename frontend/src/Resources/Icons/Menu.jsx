import React from 'react';
import Icon from "./index";


const MenuIcon = props => {
    return (
        <Icon {...props} height="24px" viewBox="0 0 24 24">
            <rect x="0" y="0" width="24" height="24"/>
            <path fillRule="evenodd" clipRule="evenodd"
                  d="M22 11.5C22 12.3284 21.3284 13 20.5 13H3.5C2.6716 13 2 12.3284 2 11.5C2 10.6716 2.6716 10 3.5 10H20.5C21.3284 10 22 10.6716 22 11.5Z"
                  fill="black"/>
            <path opacity="0.5" fillRule="evenodd" clipRule="evenodd"
                  d="M14.5 20C15.3284 20 16 19.3284 16 18.5C16 17.6716 15.3284 17 14.5 17H3.5C2.6716 17 2 17.6716 2 18.5C2 19.3284 2.6716 20 3.5 20H14.5ZM8.5 6C9.3284 6 10 5.32843 10 4.5C10 3.67157 9.3284 3 8.5 3H3.5C2.6716 3 2 3.67157 2 4.5C2 5.32843 2.6716 6 3.5 6H8.5Z"
                  fill="black"/>
        </Icon>
    )
}


export default MenuIcon;