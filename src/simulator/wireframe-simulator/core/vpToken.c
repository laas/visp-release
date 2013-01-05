/****************************************************************************
 *
 * $Id: vpToken.c 3530 2012-01-03 10:52:12Z fspindle $
 *
* This file is part of the ViSP software.
 * Copyright (C) 2005 - 2012 by INRIA. All rights reserved.
 * 
 * This software is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * ("GPL") version 2 as published by the Free Software Foundation.
 * See the file LICENSE.txt at the root directory of this source
 * distribution for additional information about the GNU GPL.
 *
 * For using ViSP with software that can not be combined with the GNU
 * GPL, please contact INRIA about acquiring a ViSP Professional 
 * Edition License.
 *
 * See http://www.irisa.fr/lagadic/visp/visp.html for more information.
 * 
 * This software was developed at:
 * INRIA Rennes - Bretagne Atlantique
 * Campus Universitaire de Beaulieu
 * 35042 Rennes Cedex
 * France
 * http://www.irisa.fr/lagadic
 *
 * If you have questions regarding the use of this file, please contact
 * INRIA at visp@inria.fr
 * 
 * This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
 * WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
 *
 * Description:
 * Le module "token.c" contient la declaration des mots cles.
 * de l'analyseur lexical "lex".
 *
 * Authors:
 * Jean-Luc CORRE
 *
 *****************************************************************************/


#include	<visp/vpMy.h>
#include	<visp/vpToken.h>

#include <visp/vpConfig.h>

#ifndef DOXYGEN_SHOULD_SKIP_THIS


Keyword	keyword_tbl[] = {	/* tableau des mots cles termine par NULL*/
	{ "above",	T_ABOVE		},
	{ "back",	T_BACK		},
	{ "below",	T_BELOW		},
	{ "bound",	T_BOUND		},
	{ "cop",	T_COP		},
	{ "depth",	T_DEPTH		},
	{ "exit",	T_EXIT		},
	{ "face_list",	T_FACE_LIST	},
	{ "front",	T_FRONT		},
	{ "left",	T_LEFT		},
	{ "none",	T_NONE		},
	{ "parallel",	T_PARALLEL	},
	{ "perspective",T_PERSPECTIVE	},
	{ "point_list",	T_POINT_LIST	},
	{ "remove",	T_REMOVE	},
	{ "right",	T_RIGHT		},
	{ "type",	T_TYPE		},
	{ "view",	T_VIEW		},
	{ "vpn",	T_VPN		},
	{ "vrp",	T_VRP		},
	{ "vup",	T_VUP		},
	{ "window",	T_WINDOW	},
	{ NULL,		NULL		}
};

#endif
