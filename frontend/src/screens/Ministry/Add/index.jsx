import React, {useState} from 'react';
import {useHistory} from 'react-router-dom';
import {FormGroup, FormInput, TextArea} from "../../../components/Forms";
import Button from "../../../components/Button";
import ArrowLeftIcon from "../../../Resources/Icons/ArrowLeft";
import CheckIcon from "../../../Resources/Icons/Check";
import ArrowRightIcon from "../../../Resources/Icons/ArrowRight";
import SubHeader from "../../../components/Subheader";
import axios from "axios";


const AddPage = () => {
    const [name, setName] = useState("")
    const [description, setDescription] = useState("")

    const history = useHistory()

    const addMinistry = e => {
        const data = {
            name, description
        }

        console.log(data)

        axios.post("/api/ministry/", data)
            .then(response => {
                history.push("/ministry/list/")
            })
            .catch(error => {
                console.log(error.response)
            })
    }

    return (
        <>
            <SubHeader title={"Add Ministry"} description={"Enter Ministry's Details"}/>
            <div className={"d-flex flex-column-fluid"}>
                <div className={"container mt-5"}>
                    <div className={"card card-custom card-transparent mt-5"}>
                        <div className={"card-body p-0 mt-5"}>
                            <div className={"card card-custom card-shadowless rounded-top-0"}>
                                <div className={"card-body p-0"}>
                                    <div className="row justify-content-center py-8 px-8 py-lg-15 px-lg-10">
                                        <div className="col-xl-12 col-xxl-10">
                                            <FormGroup>
                                                <FormInput
                                                    value={name} onChange={e => setName(e.target.value)}
                                                    containerClass={"col-lg-9 col-xl-9"} solid lg type={"text"}
                                                    label={"Name"} placeholder={"E.g Ushering"}/>

                                                <TextArea value={description}
                                                          onChange={e => setDescription(e.target.value)}
                                                          rows={5} containerClass={"col-lg-9 col-xl-9 mt-5"} solid lg
                                                          type={"text"}
                                                          label={"Description"}
                                                          placeholder={"E.g Taking of the church..."}/>
                                                <div className="w-100 pr-5">
                                                    <Button onClick={addMinistry}
                                                            className={"px-10 py-3 mt-15 ml-15 float-right"}
                                                            bg={"primary"}>Add Member</Button>
                                                </div>
                                            </FormGroup>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}


export default AddPage