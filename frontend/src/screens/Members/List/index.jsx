import React, {useEffect, useState} from 'react'
import {Link} from 'react-router-dom';
import axios from "axios";
import DataTable from 'react-data-table-component';
import EditIcon from "../../../Resources/Icons/Edit";
import TrashIcon from "../../../Resources/Icons/Trash";
import ViewIcon from "../../../Resources/Icons/View";


export const SubHeader = props => {
    return (
        <div className="subheader py-2 py-lg-6 subheader-transparent" id="kt_subheader">
            <div className="container d-flex align-items-center justify-content-between flex-wrap flex-sm-nowrap">
                { /* begin::Details */}
                <div className="d-flex align-items-center flex-wrap mr-2">
                    { /* begin::Title */}
                    <h5 className="text-dark font-weight-bold mt-2 mb-2 mr-5">{props.title}</h5>
                    { /* end::Title */}
                    { /* begin::Separator */}
                    <div className="subheader-separator subheader-separator-ver mt-2 mb-2 mr-5 bg-gray-300"></div>
                    { /* end::Separator */}
                    { /* begin::Search Form */}
                    <div className="d-flex align-items-center" id="kt_subheader_search">
                        <span className="text-dark-50 font-weight-bold" id="kt_subheader_total">{props.total} Total</span>
                        <form className="ml-5">
                            <div className="input-group input-group-sm bg-white border-0 rounded min-w-175px">
                                <input type="text" className="form-control bg-white border-0"
                                       id="kt_subheader_search_form" placeholder="Search..."/>
                            </div>
                        </form>
                    </div>
                    { /* end::Search Form */}
                </div>
                { /* end::Details */}
                { /* begin::Toolbar */}
                <div className="d-flex align-items-center">
                    { /* begin::Button */}
                    <a href="#" className="font-weight-bolder font-size-sm px-5 btn-fixed-height"></a>
                    { /* end::Button */}
                    { /* begin::Button */}
                    <Link to={props.primaryActionLink}
                       className="btn btn-bg-white btn-text-dark-50 btn-hover-text-primary btn-icon-primary btn-fixed-height font-weight-bolder font-size-sm px-5 ml-2">
                        {props.primaryActionText}
                    </Link>
                    { /* end::Button */}
                    { /* begin::Dropdown */}
                    <div className="dropdown dropdown-inline ml-2" data-toggle="tooltip" title="Quick actions"
                         data-placement="top">
                        <a href="#" className="btn btn-fixed-height btn-primary font-weight-bolder font-size-sm px-5"
                           data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Quick Actions</a>
                    </div>
                    { /* end::Dropdown */}
                </div>
                { /* end::Toolbar */}
            </div>
        </div>
    )
}


export const Table = props => {
    return (
        <div className="d-flex flex-column-fluid">
            {/* begin::Container */}
            <div className="container">
                {/* begin::Card */}
                <div className="card card-custom">
                    {/* begin::Header */}
                    <div className="card-header flex-wrap border-0 pt-6 pb-0">
                        <div className="card-title">
                            <h3 className="card-label">{props.title} Listing
                                <span
                                    className="d-block text-muted pt-2 font-size-sm">{props.title} listing &amp; management</span>
                            </h3>
                        </div>
                    </div>
                    {/* end::Header */}
                    {/* begin::Body */}
                    <div className="card-body">
                        {/* begin: Datatable */}
                        {props.children}
                        {/* end: Datatable */}
                    </div>
                    {/* end::Body */}
                </div>
                {/* end::Card */}
            </div>
            {/* end::Container */}
        </div>
    )
}


const EntryActions = () => {
    return (
        <>
            <span style={{overflow: "visible", position: "relative", width: 130}}>
                <a title={"View Details"} href="#"
                   className="btn btn-sm btn-default btn-text-primary btn-hover-primary btn-icon mr-2">
                    <ViewIcon />
                </a>
                <a href="#"
                   className="btn btn-sm btn-default btn-text-primary btn-hover-primary btn-icon mr-2"
                   title="Edit details">
                    <EditIcon />
                </a>
                <a href="#"
                   className="btn btn-sm btn-default btn-text-primary btn-hover-primary btn-icon"
                   title="Delete">
                    <TrashIcon />
                </a>
            </span>
        </>
    )
}

const EntryTable = () => {
    const [members, setMembers] = useState([])

    useEffect(() => {
        axios.get("/member/")
            .then(response => {
                setMembers(response.data.members)
                console.log(response.data.members[2])
            })
            .catch(error => {
                console.log(error.response)
            })
    }, [])

    const columns = [
        {
            name: "First Name",
            selector: "first_name",
            sortable: true
        },
        {
            name: "Last Name",
            selector: "last_name",
            sortable: true
        },
        {
            name: "Contact",
            selector: "contact_1",
        },
        {
            name: "Ministry",
            selector: "ministry",
            sortable: true
        },
        {
            name: "",
            selector: "",
            sortable: true
        },
        {
            name: "Actions",
            cell: row => <EntryActions />
        }
    ]

    return (

        <DataTable total={members.length} title={"Members"} columns={columns} data={members}/>
    )
}

const ListPage = () => {

    return (
        <>
            <SubHeader primaryActionText={"Add User"} primaryActionLink={"/members/add/"} title={"Members"}/>
            <Table>
                <EntryTable/>
            </Table>
        </>
    )
}


export default ListPage;