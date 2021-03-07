#//----------------------------------------------------------------------
#// Copyright 2010-2011 Mentor Graphics Corporation
#// Copyright 2014 Semifore
#// Copyright 2010-2017 Synopsys, Inc.
#// Copyright 2010-2018 Cadence Design Systems, Inc.
#// Copyright 2014-2015 NVIDIA Corporation
#//   Copyright 2019-2020 Tuomas Poikela (tpoikela)
#//   All Rights Reserved Worldwide
#//
#//   Licensed under the Apache License, Version 2.0 (the
#//   "License"); you may not use this file except in
#//   compliance with the License.  You may obtain a copy of
#//   the License at
#//
#//       http://www.apache.org/licenses/LICENSE-2.0
#//
#//   Unless required by applicable law or agreed to in
#//   writing, software distributed under the License is
#//   distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#//   CONDITIONS OF ANY KIND, either express or implied.  See
#//   the License for the specific language governing
#//   permissions and limitations under the License.
#//----------------------------------------------------------------------
#
from enum import Enum, auto
from uvm.macros.uvm_message_defines import uvm_error
import cocotb

#// File -- NODOCS -- TLM2 Types
#typedef class uvm_time
#
#// Enum -- NODOCS -- uvm_tlm_phase_e
#//
#// Nonblocking transport synchronization state values between
#// an initiator and a target.
#//
#//  UNINITIALIZED_PHASE  - Defaults for constructor
#//  BEGIN_REQ            - Beginning of request phase
#//  END_REQ              - End of request phase
#//  BEGIN_RESP           - Beginning of response phase
#//  END_RESP             - End of response phase
#

class uvm_tlm_phase_e(Enum):
    UNINITIALIZED_PHASE = auto()
    BEGIN_REQ = auto()
    END_REQ = auto()
    BEGIN_RESP = auto()
    END_RESP = auto()


#// Enum -- NODOCS -- uvm_tlm_sync_e
#//
#// Pre-defined phase state values for the nonblocking transport
#// Base Protocol between an initiator and a target.
#//
#// UVM_TLM_ACCEPTED      - Transaction has been accepted
#// UVM_TLM_UPDATED       - Transaction has been modified
#// UVM_TLM_COMPLETED     - Execution of transaction is complete

class uvm_tlm_sync_e(Enum):
    UVM_TLM_ACCEPTED = auto()
    UVM_TLM_UPDATED = auto()
    UVM_TLM_COMPLETED = auto()

#// Defines Not-Yet-Implemented TLM tasks
UVM_TLM_TASK_ERROR="TLM-2 interface task not implemented"

#// Defines Not-Yet-Implemented TLM functions
UVM_TLM_FUNCTION_ERROR="TLM-2 interface function not implemented"

#//
#// Class -- NODOCS -- uvm_tlm_if
#//
#// Base class type to define the transport functions.
#//
#//  -  <nb_transport_fw>
#//
#//  - <nb_transport_bw>
#//
#//  - <b_transport>
#//

class UVMTLMIf():

    #//----------------------------------------------------------------------
    #// Group: tlm transport methods
    #//
    #// Each of the interface methods take a handle to the transaction to be
    #// transported and a reference argument for the delay. In addition, the
    #// nonblocking interfaces take a reference argument for the phase.
    #//

    #//----------------------------------------------------------------------
    #// Function: nb_transport_fw
    #//
    #// Forward path call.
    #// The first call to this method for a transaction marks the initial timing point.
    #// Every call to this method may mark a timing point in the execution of the
    #// transaction. The timing annotation argument allows the timing points
    #// to be offset from the simulation times at which the forward path is used.
    #// The final timing point of a transaction may be marked by a call
    #// to <nb_transport_bw> or a return from this or subsequent call to
    #// nb_transport_fw.
    #//
    #// See <TLM2 Interfaces, Ports, Exports and Transport Interfaces Subset>
    #// for more details on the semantics and rules of the nonblocking
    #// transport interface.
    def nb_transport_fw(self, t, p, delay):
        uvm_error("nb_transport_fw", UVM_TLM_FUNCTION_ERROR)
        return uvm_tlm_sync_e.UVM_TLM_ACCEPTED

    #// Function: nb_transport_bw
    #//
    #// Implementation of the backward path.
    #// This function MUST be implemented in the INITIATOR component class.
    #//
    #// Every call to this method may mark a timing point, including the final
    #// timing point, in the execution of the transaction.
    #// The timing annotation argument allows the timing point
    #// to be offset from the simulation times at which the backward path is used.
    #// The final timing point of a transaction may be marked by a call
    #// to <nb_transport_fw> or a return from this or subsequent call to
    #// nb_transport_bw.
    #//
    #// See <TLM2 Interfaces, Ports, Exports and Transport Interfaces Subset>
    #// for more details on the semantics and rules of the nonblocking
    #// transport interface.
    #//
    #// Example:
    #//
    #//| class master extends uvm_component;
    #//     uvm_tlm_nb_initiator_socket #(trans, uvm_tlm_phase_e, this_t) initiator_socket;
    #//|    ...
    #//|    function void build_phase(uvm_phase phase);
    #//        initiator_socket = new("initiator_socket", this, this);
    #//|    endfunction
    #//|
    #//|    function uvm_tlm_sync_e nb_transport_bw(ref trans t,
    #//|                                   ref uvm_tlm_phase_e p,
    #//|                                   input uvm_tlm_time delay);
    #//|        transaction = t;
    #//|        state = p;
    #//|        return UVM_TLM_ACCEPTED;
    #//|    endfunction
    #//|
    #//|    ...
    #//| endclass
    def nb_transport_bw(self, t, p, delay):
        uvm_error("nb_transport_bw", UVM_TLM_FUNCTION_ERROR)
        return uvm_tlm_sync_e.UVM_TLM_ACCEPTED

    #// Function: b_transport
    #//
    #// Execute a blocking transaction. Once this method returns,
    #// the transaction is assumed to have been executed. Whether
    #// that execution is successful or not must be indicated by the
    #// transaction itself.
    #//
    #// The callee may modify or update the transaction object, subject
    #// to any constraints imposed by the transaction class. The
    #// initiator may re-use a transaction object from one call to
    #// the next and across calls to b_transport().
    #//
    #// The call to b_transport shall mark the first timing point of the
    #// transaction. The return from b_transport shall mark the final
    #// timing point of the transaction. The timing annotation argument
    #// allows the timing points to be offset from the simulation times
    #// at which the task call and return are executed.
    @cocotb.coroutine
    def b_transport(self, t, delay):
        uvm_error("b_transport", UVM_TLM_TASK_ERROR)
