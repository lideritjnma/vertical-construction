# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the Affero GNU General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    Affero GNU General Public License for more details.
#
#    You should have received a copy of the Affero GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

{
    "name" : "Insulation Products",
    "version" : "0.2",
    "author" : "Savoir-faire Linux",
    "website" : "http://www.savoirfairelinux.com",
    "license" : "AGPL-3",
    "category" : "Product",
    "description" : """
    This module allows you to define if a product is an insulation product, by 
    adding a checkbox on the product form. Checking the box enables you to enter
    the R-value (thermal resistance) of the product and specify if the insulation
    is spray foam.

    Insulation products are sold in square foot (UOS) and stored in PCE or weight.
    Spray foam products are sold in board foot (UOS), calculated from the product 
    R-value, the sale order line R-value and the area (in sq ft).

    More information about the R-value here:
    http://en.wikipedia.org/wiki/R-value_(insulation)
    """,
    "images" : ["images/product_insulation.png"],
    "depends" : ["product"],
    "demo" : [],
    "test" : [],
    "data" : [
	"product_insulation_data.xml",
	"product_insulation_view.xml",
	],
    "installable": True,
    "complexity": "easy",
}
