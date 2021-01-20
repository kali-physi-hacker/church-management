import React from "react";
import Wizard from "../../../components/Wizard";
import SubHeader from "../../../components/Subheader";


const AddPage = () => {
    return (
        <>
            <SubHeader title={"Add User"} description={"Enter User's Information"}/>
            <div className={"d-flex flex-column-fluid"}>
                <div className={"container"}>
                    <div className={"card card-custom card-transparent"}>
                        <div className={"card-body p-0"}>
                            <Wizard/>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}


export default AddPage;