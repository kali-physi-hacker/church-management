import React, {useState, useEffect} from 'react';
import axios from "axios";
import DataTable from 'react-data-table-component';
import {SubHeader, Table} from "../../Members/List/index";


const MTable = () => {
    const [ministries, setMinistries] = useState([])

    const columns = [
        {
            name: "Name",
            selector: "name",
            sortable: true
        },
        {
            name: "Description",
            selector: "description",
            sortable: true
        }
    ]

    useEffect(() => {
        axios.get("/ministry/")
            .then(response => {
                setMinistries(response.data.ministries)
                console.log("Length:", ministries.length)
            })
            .catch(error => {
                console.log(error.response)
            })
    }, [])
    return (
        <>
            <Table>
                <DataTable total={ministries.length} title={"Ministries"} columns={columns} data={ministries}/>
            </Table>
        </>
    )
}

const ListPage = () => {
    return (
        <>
            <SubHeader primaryActionText={"Add Ministry"} primaryActionLink={"/ministry/add/"} title={"Ministries"}/>
            <MTable />
        </>
    )
}


export default ListPage