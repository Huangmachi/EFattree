# Copyright (C) 2016 Li Cheng at Beijing University of Posts
# and Telecommunications. www.muzixing.com
# Copyright (C) 2016 Huang MaChi at Chongqing University
# of Posts and Telecommunications, Chongqing, China.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
	Common Setting for EFattree.
"""

DISCOVERY_PERIOD = 10   # For discovering topology.

MONITOR_PERIOD = 5   # For monitoring traffic

TOSHOW_topo = True	   # For showing network topology in terminal
TOSHOW_stat = True	   # For showing statistics in terminal
TOSHOW_flow_stat = True	   # For showing flow statistics in terminal
TOSHOW_port_stat = False	   # For showing port statistics in terminal

MAX_CAPACITY = 10000   # Max capacity of link

# List the port numbers of bandwidth-sensitive service
bw_sensitive_port_list = [5001]
