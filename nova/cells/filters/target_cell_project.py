# Copyright (c) 2014 CERN
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Project target cell filter.
"""

from nova.cells import filters

class TargetCellProjectFilter(filters.BaseCellFilter):
    """Target Cell Project Filter"""

    def filter_all(self, cells, filter_properties):
        """Override filter_all() which operates on the full list
        of cells...
        """
        request_spec = filter_properties.get('request_spec', {})
        instance_properties = request_spec['instance_properties']
        instance_project_id = instance_properties['project_id']

        project_cells = []
        generic_cells = []

        for cell in cells:
            projects = cell.capabilities.get('projects')
            if projects != None:
                if instance_project_id in projects:
                    project_cells.append(cell)
            else:
                generic_cells.append(cell)

        if project_cells != []:
            return project_cells

        return generic_cells

