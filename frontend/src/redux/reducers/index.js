import {combineReducers} from "redux";

import sidebarReducer from "./sidebar";


const rootReducer = combineReducers({
    sidebar: sidebarReducer
})

export default rootReducer;