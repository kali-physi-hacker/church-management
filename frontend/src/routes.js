import {Route, Switch} from 'react-router-dom';

import AddPage from "./screens/Members/Add";


const Routes = () => {
    return (
        <Switch>
            <Route path={"/member/add"} component={AddPage} />
        </Switch>
    )
}


export default Routes;