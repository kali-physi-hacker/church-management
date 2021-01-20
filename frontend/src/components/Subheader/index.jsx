import React from 'react';
import FileIcon from "../../Resources/Icons/File";
import Button from "../Button";
import DropdownMenu, {Nav, NavItem} from "../Dropdown";


const ButtonGroup = props => {
    return (
        <div className="btn-group ml-2">
            <Button bg={"primary"} weight={"bolder"} fontSize={"sm"} className={"px-5 btn-fixed-height"}>Submit</Button>
            <Button bg={"primary"} weight={"bolder"} fontSize={"sm"}
                    className={"px-3 btn-fixed-height dropdown-toggle dropdown-toggle-split"}/>
            <DropdownMenu size={"sm"} side={"right"} className={"p-0 m-0"}>
                <Nav className={"py-5"}>
                    <NavItem link text={"Save & continue"}/>
                    <NavItem link text={"Save & add new"}/>
                    <NavItem link text={"Save & exit"}/>
                </Nav>
            </DropdownMenu>
        </div>
    )
}

const HeaderDetails = props => {
    return (
        <div className="d-flex align-items-center flex-wrap mr-2">
            <h5 className="text-dark font-weight-bold mt-2 mb-2 mr-5">{props.title}</h5>
            <div className="subheader-separator subheader-separator-ver mt-2 mb-2 mr-5 bg-gray-300"></div>
            <div className="d-flex align-items-center" id="kt_subheader_search">
                <span className="text-dark-50 font-weight-bold"
                      id="kt_subheader_total">{props.description}</span>
            </div>
        </div>
    )
}


const Toolbar = props => {
    return (
        <div className="d-flex align-items-center">
            <a href="#"
               className="btn btn-white btn-hover-bg-white btn-hover-text-primary font-weight-bold font-weight-bolder font-size-sm px-5 btn-fixed-height">Back</a>
            <ButtonGroup/>
            <div className="dropdown dropdown-inline ml-2" data-toggle="tooltip" title="Quick actions"
                 data-placement="top">
                <a href="#" className="btn btn-fixed-height btn-primary font-weight-bolder font-size-sm px-5"
                   data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    <FileIcon size={"md"}/> Quick Actions</a>
                <div className="dropdown-menu dropdown-menu-md dropdown-menu-right p-0 m-0">
                    <ul className="navi navi-hover">
                        <NavItem>
                            <span className="navi-text">
                                <span
                                    className="label label-xl label-inline label-light-primary">Orders</span>
                            </span>
                        </NavItem>
                        <li className="navi-header font-weight-bold py-4">
                            <span className="font-size-lg">Choose Option:</span>
                            <i className="flaticon2-information icon-md text-muted" data-toggle="tooltip"
                               data-placement="right" title="Click to learn more..."></i>
                        </li>
                        <li className="navi-separator mb-3 opacity-70"></li>
                        <li className="navi-item">
                            <a href="#" className="navi-link">
														<span className="navi-text">
															<span
                                                                className="label label-xl label-inline label-light-primary">Orders</span>
														</span>
                            </a>
                        </li>
                        <li className="navi-item">
                            <a href="#" className="navi-link">
														<span className="navi-text">
															<span
                                                                className="label label-xl label-inline label-light-danger">Reports</span>
														</span>
                            </a>
                        </li>
                        <li className="navi-item">
                            <a href="#" className="navi-link">
														<span className="navi-text">
															<span
                                                                className="label label-xl label-inline label-light-warning">Tasks</span>
														</span>
                            </a>
                        </li>
                        <li className="navi-item">
                            <a href="#" className="navi-link">
														<span className="navi-text">
															<span
                                                                className="label label-xl label-inline label-light-success">Events</span>
														</span>
                            </a>
                        </li>
                        <li className="navi-item">
                            <a href="#" className="navi-link">
														<span className="navi-text">
															<span
                                                                className="label label-xl label-inline label-light-dark">Members</span>
														</span>
                            </a>
                        </li>
                        <li className="navi-separator mt-3 opacity-70"></li>
                        <li className="navi-footer py-4">
                            <a className="btn btn-primary font-weight-bold btn-sm px-5" href="#">
                                <i className="ki ki-plus icon-sm"></i>Create</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    )
}

const SubHeader = props => {
    return (
        <div className="subheader py-2 py-lg-6 subheader-transparent" id="kt_subheader">
            <div className="container d-flex align-items-center justify-content-between flex-wrap flex-sm-nowrap">
                <HeaderDetails {...props} />
                <Toolbar {...props} />
            </div>
        </div>
    )
}


export default SubHeader