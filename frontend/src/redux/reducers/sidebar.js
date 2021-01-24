import {OPEN_SIDEBAR, CLOSE_SIDEBAR} from "../actions/sidebar";

const initialState = {
    isOpened: true
}


const sidebarReducer = (state = initialState, action) => {
    switch (action.type) {
        case OPEN_SIDEBAR:
            return {
                ...state,
                isOpened: true
            }

        case CLOSE_SIDEBAR:
            return {
                ...state,
                isOpened: false
            }

        default:
            return state;
    }
}


export default sidebarReducer;