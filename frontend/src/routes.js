import {Route, Switch} from 'react-router-dom';

import memberAdd from "./screens/Members/Add";
import memberList from "./screens/Members/List";
import ministriesList from "./screens/Ministry/List";
import ministriesAdd from "./screens/Ministry/Add/index.jsx";


const Routes = () => {
    return (
        <Switch>
            <Route path={"/member/add"} component={memberAdd} />
            <Route path={"/member/list"} component={memberList} />
            <Route path={"/ministry/list/"} component={ministriesList} />
            <Route path={"/ministry/add/"} component={ministriesAdd} />
        </Switch>
    )
}


export default Routes;