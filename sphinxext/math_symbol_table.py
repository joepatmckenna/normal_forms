





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://assets-cdn.github.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-e04a23d39bf81b7db3c635177756ef51bc171feb440be9e174933c6eb56382da.css" integrity="sha256-4Eoj05v4G32zxjUXd1bvUbwXH+tEC+nhdJM8brVjgto=" media="all" rel="stylesheet" />
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-3dc65358913934c77ed38ef6979525393a285062908a13a901527639c133c821.css" integrity="sha256-PcZTWJE5NMd+0472l5UlOTooUGKQihOpAVJ2OcEzyCE=" media="all" rel="stylesheet" />
  
  
  
  

  <meta name="viewport" content="width=device-width">
  
  <title>matplotlib/math_symbol_table.py at master · matplotlib/matplotlib</title>
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta content="https://avatars0.githubusercontent.com/u/215947?v=3&amp;s=400" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="matplotlib/matplotlib" property="og:title" /><meta content="https://github.com/matplotlib/matplotlib" property="og:url" /><meta content="matplotlib: plotting with Python" property="og:description" />

  <link rel="assets" href="https://assets-cdn.github.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6MTc5NjE5NDk5OjI4N2Y5MmU1MjA2YWU1ZDY5Y2RhYTA2MTIwM2IwNzZlNzIyMjQxY2ZlM2Q3ZDgyOGZmZDQ3NTQzMWMzNTkwNjY=--edf0b90ae98a959a16f3bf536e1b5c51ac26c765">
  <meta name="pjax-timeout" content="1000">
  <link rel="sudo-modal" href="/sessions/sudo_modal">
  <meta name="request-id" content="BD6A:1E56:57A067:83A4D5:59571381" data-pjax-transient>
  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="https://collector.githubapp.com/github-external/browser_event" name="octolytics-event-url" /><meta content="BD6A:1E56:57A067:83A4D5:59571381" name="octolytics-dimension-request_id" /><meta content="iad" name="octolytics-dimension-region_edge" /><meta content="iad" name="octolytics-dimension-region_render" /><meta content="16746032" name="octolytics-actor-id" /><meta content="joepatmckenna" name="octolytics-actor-login" /><meta content="ab8f802b26f103069d2b89d19f550f8cb4e52f41748e426e5410de59f5457619" name="octolytics-actor-hash" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />




  <meta class="js-ga-set" name="dimension1" content="Logged In">


  

      <meta name="hostname" content="github.com">
  <meta name="user-login" content="joepatmckenna">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="N2JiYWM0ZjM3NTBmZDYxZmNkNTdkNzI2OWQyZTY2YTM0MGM0ODFjZmM0MjkxMDZmMjlmMzMzOTg4ZmVhZmNiYnx7InJlbW90ZV9hZGRyZXNzIjoiOTguMjQ0LjI0Ni4yMzAiLCJyZXF1ZXN0X2lkIjoiQkQ2QToxRTU2OjU3QTA2Nzo4M0E0RDU6NTk1NzEzODEiLCJ0aW1lc3RhbXAiOjE0OTg4Nzg4NTYsImhvc3QiOiJnaXRodWIuY29tIn0=">


  <meta name="html-safe-nonce" content="1581b23ba9a1b3331b8822801a7ef5e5b5b162d4">

  <meta http-equiv="x-pjax-version" content="e87457103958760f131cc966530f53fd">
  

      <link href="https://github.com/matplotlib/matplotlib/commits/master.atom" rel="alternate" title="Recent Commits to matplotlib:master" type="application/atom+xml">

  <meta name="description" content="matplotlib: plotting with Python">
  <meta name="go-import" content="github.com/matplotlib/matplotlib git https://github.com/matplotlib/matplotlib.git">

  <meta content="215947" name="octolytics-dimension-user_id" /><meta content="matplotlib" name="octolytics-dimension-user_login" /><meta content="1385122" name="octolytics-dimension-repository_id" /><meta content="matplotlib/matplotlib" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="1385122" name="octolytics-dimension-repository_network_root_id" /><meta content="matplotlib/matplotlib" name="octolytics-dimension-repository_network_root_nwo" /><meta content="false" name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" />


    <link rel="canonical" href="https://github.com/matplotlib/matplotlib/blob/master/doc/sphinxext/math_symbol_table.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">


  <meta name="u2f-support" content="true">

  </head>

  <body class="logged-in env-production page-blob">
    



  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="bg-black text-white p-3 show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    



        
<div class="header" role="banner">
  <div class="container clearfix">
    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg aria-hidden="true" class="octicon octicon-mark-github" height="32" version="1.1" viewBox="0 0 16 16" width="32"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>


        <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/matplotlib/matplotlib/search" class="js-site-search-form" data-scoped-search-url="/matplotlib/matplotlib/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
        <a href="/matplotlib/matplotlib/blob/master/doc/sphinxext/math_symbol_table.py" class="header-search-scope no-underline">This repository</a>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        value=""
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
        <input type="hidden" class="js-site-search-type-field" name="type" >
    </label>
</form></div>


      <ul class="header-nav float-left" role="navigation">
        <li class="header-nav-item">
          <a href="/pulls" aria-label="Pull requests you created" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:pulls context:user" data-hotkey="g p" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls">
            Pull requests
</a>        </li>
        <li class="header-nav-item">
          <a href="/issues" aria-label="Issues you created" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:issues context:user" data-hotkey="g i" data-selected-links="/issues /issues/assigned /issues/mentioned /issues">
            Issues
</a>        </li>
            <li class="header-nav-item">
              <a href="/marketplace" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-selected-links=" /marketplace">
                Marketplace
</a>            </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com/" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
      </ul>

    
<ul class="header-nav user-nav float-right" id="user-links">
  <li class="header-nav-item">
    

  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link tooltipped tooltipped-s js-menu-target" href="/new"
       aria-label="Create new…"
       aria-expanded="false"
       aria-haspopup="true"
       data-ga-click="Header, create new, icon:add">
      <svg aria-hidden="true" class="octicon octicon-plus float-left" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5z"/></svg>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="matplotlib/matplotlib">This repository</span>
  </div>
    <a class="dropdown-item" href="/matplotlib/matplotlib/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>

      </ul>
    </div>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name tooltipped tooltipped-sw js-menu-target" href="/joepatmckenna"
       aria-label="View profile and more"
       aria-expanded="false"
       aria-haspopup="true"
       data-ga-click="Header, show menu, icon:avatar">
      <img alt="@joepatmckenna" class="avatar" src="https://avatars1.githubusercontent.com/u/16746032?v=3&amp;s=40" height="20" width="20">
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <div class="dropdown-menu dropdown-menu-sw">
        <div class="dropdown-header header-nav-current-user css-truncate">
          Signed in as <strong class="css-truncate-target">joepatmckenna</strong>
        </div>

        <div class="dropdown-divider"></div>

        <a class="dropdown-item" href="/joepatmckenna" data-ga-click="Header, go to profile, text:your profile">
          Your profile
        </a>
        <a class="dropdown-item" href="/joepatmckenna?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a>
        <a class="dropdown-item" href="/explore" data-ga-click="Header, go to explore, text:explore">
          Explore
        </a>
        <a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a>

        <div class="dropdown-divider"></div>

        <a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
          Settings
        </a>

        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="BZ1qipUbQlBY29pgddjSCZHm2Q8g0FVNpecI9Hu71Sl+4ldVnFG6k8LtP5aUrOTIE9EJdC8/z5UR7YUueBNVig==" /></div>
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </li>
</ul>


    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/logout" class="sr-only right-0" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="UVSZiw+w45DHcWr67JsAiN0bV7qHYj72duWoE8UQUGQqK6RUBvobU11HjwwN7zZJXyyHwYiNpC7C7yXJxrjQxw==" /></div>
      <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
        Sign out
      </button>
</form>  </div>
</div>


      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">
</div>



  <div role="main">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode">
    <div id="js-repo-pjax-container" data-pjax-container>
      



  


    <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
      <div class="container repohead-details-container">

        <ul class="pagehead-actions">
  <li>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="waham75BWs28fB9nyMADOrtglLM/zemYJcv2cN9KyJiqddsJ3XrJ8pIuuspwMFkBfGh7QjaZ9oNrOf20s4kXQQ==" /></div>      <input class="form-control" id="repository_id" name="repository_id" type="hidden" value="1385122" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/matplotlib/matplotlib/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target"
            role="button"
            aria-haspopup="true"
            aria-expanded="false"
            aria-label="Toggle repository notifications menu"
            data-ga-click="Repository, click Watch settings, action:blob#show">
            <span class="js-select-button">
                <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                Watch
            </span>
          </a>
            <a class="social-count js-social-count"
              href="/matplotlib/matplotlib/watchers"
              aria-label="435 users are watching this repository">
              435
            </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content">
            <div class="select-menu-header js-navigation-enable" tabindex="-1">
              <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                        Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input id="do_ignore" name="do" type="radio" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-mute" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                        Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/matplotlib/matplotlib/unstar" class="starred" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="4Soy1Yx9V/OAkryhOfxBDjuGiXg+YTKraVD+4f1VebuNzOsDGCcOCYrD3ZO+aRXtbPuwbVQEz6Vi+Bl5NnwPBw==" /></div>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar matplotlib/matplotlib"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/matplotlib/matplotlib/stargazers"
           aria-label="5470 users starred this repository">
          5,470
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/matplotlib/matplotlib/star" class="unstarred" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="C2FZFR5OfQ29vR2tfpywLttygabs/1PskAWXXX70/vQOymkuQU/pPXP6qTfEnREA8qxlRiavrqmWfcCeobTCfg==" /></div>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star matplotlib/matplotlib"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Star
      </button>
        <a class="social-count js-social-count" href="/matplotlib/matplotlib/stargazers"
           aria-label="5470 users starred this repository">
          5,470
        </a>
</form>  </div>

  </li>

  <li>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/matplotlib/matplotlib/fork" class="btn-with-count" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="DnZpF/8GsZWPu/tMXEt05SoNoR1Le4DW9d9uB/Tlon/7rJ65K5rkQAUtTNWFu1CKbyOCZY9sr9vo9B8Ph9/36Q==" /></div>
            <button
                type="submit"
                class="btn btn-sm btn-with-count"
                data-ga-click="Repository, show fork modal, action:blob#show; text:Fork"
                title="Fork your own copy of matplotlib/matplotlib to your account"
                aria-label="Fork your own copy of matplotlib/matplotlib to your account">
              <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
              Fork
            </button>
</form>
    <a href="/matplotlib/matplotlib/network" class="social-count"
       aria-label="2629 users forked this repository">
      2,629
    </a>
  </li>
</ul>

        <h1 class="public ">
  <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a href="/matplotlib" class="url fn" rel="author">matplotlib</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/matplotlib/matplotlib" data-pjax="#js-repo-pjax-container">matplotlib</a></strong>

</h1>

      </div>
      <div class="container">
        
<nav class="reponav js-repo-nav js-sidenav-container-pjax"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/matplotlib/matplotlib" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /matplotlib/matplotlib" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/matplotlib/matplotlib/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /matplotlib/matplotlib/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">985</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/matplotlib/matplotlib/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /matplotlib/matplotlib/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">230</span>
      <meta itemprop="position" content="3">
</a>  </span>

    <a href="/matplotlib/matplotlib/projects" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /matplotlib/matplotlib/projects">
      <svg aria-hidden="true" class="octicon octicon-project" height="16" version="1.1" viewBox="0 0 15 16" width="15"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >5</span>
</a>
    <a href="/matplotlib/matplotlib/wiki" class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /matplotlib/matplotlib/wiki">
      <svg aria-hidden="true" class="octicon octicon-book" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"/></svg>
      Wiki
</a>

    <div class="reponav-dropdown js-menu-container">
      <button type="button" class="btn-link reponav-item reponav-dropdown js-menu-target " data-no-toggle aria-expanded="false" aria-haspopup="true">
        Insights
        <svg aria-hidden="true" class="octicon octicon-triangle-down v-align-middle text-gray" height="11" version="1.1" viewBox="0 0 12 16" width="8"><path fill-rule="evenodd" d="M0 5l6 6 6-6z"/></svg>
      </button>
      <div class="dropdown-menu-content js-menu-content">
        <div class="dropdown-menu dropdown-menu-sw">
          <a class="dropdown-item" href="/matplotlib/matplotlib/pulse" data-skip-pjax>
            <svg aria-hidden="true" class="octicon octicon-pulse" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M11.5 8L8.8 5.4 6.6 8.5 5.5 1.6 2.38 8H0v2h3.6l.9-1.8.9 5.4L9 8.5l1.6 1.5H14V8z"/></svg>
            Pulse
          </a>
          <a class="dropdown-item" href="/matplotlib/matplotlib/graphs" data-skip-pjax>
            <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
            Graphs
          </a>
        </div>
      </div>
    </div>
</nav>

      </div>
    </div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    
  <a href="/matplotlib/matplotlib/blob/9da6cb6cdf4eb3c2508de96d7243abd82ff487a0/doc/sphinxext/math_symbol_table.py" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>

  <!-- blob contrib key: blob_contributors:v21:08709353ab74fa33b08ec5343894131e -->

  <div class="file-navigation js-zeroclipboard-container">
    
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" aria-expanded="false" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/matplotlib/matplotlib/blob/master/doc/sphinxext/math_symbol_table.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/matplotlib/matplotlib/blob/v2.0.x/doc/sphinxext/math_symbol_table.py"
               data-name="v2.0.x"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                v2.0.x
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/matplotlib/matplotlib/blob/v2.0.2-doc/doc/sphinxext/math_symbol_table.py"
               data-name="v2.0.2-doc"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                v2.0.2-doc
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v2.0.2/doc/sphinxext/math_symbol_table.py"
              data-name="v2.0.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.0.2">
                v2.0.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v2.0.1/doc/sphinxext/math_symbol_table.py"
              data-name="v2.0.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.0.1">
                v2.0.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v2.0.0/doc/sphinxext/math_symbol_table.py"
              data-name="v2.0.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.0.0">
                v2.0.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v2.0.0rc2/doc/sphinxext/math_symbol_table.py"
              data-name="v2.0.0rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.0.0rc2">
                v2.0.0rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v2.0.0rc1/doc/sphinxext/math_symbol_table.py"
              data-name="v2.0.0rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.0.0rc1">
                v2.0.0rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v2.0.0b4/doc/sphinxext/math_symbol_table.py"
              data-name="v2.0.0b4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.0.0b4">
                v2.0.0b4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v2.0.0b3/doc/sphinxext/math_symbol_table.py"
              data-name="v2.0.0b3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.0.0b3">
                v2.0.0b3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v2.0.0b2/doc/sphinxext/math_symbol_table.py"
              data-name="v2.0.0b2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.0.0b2">
                v2.0.0b2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v2.0.0b1/doc/sphinxext/math_symbol_table.py"
              data-name="v2.0.0b1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.0.0b1">
                v2.0.0b1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.5.3/doc/sphinxext/math_symbol_table.py"
              data-name="v1.5.3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.5.3">
                v1.5.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.5.2/doc/sphinxext/math_symbol_table.py"
              data-name="v1.5.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.5.2">
                v1.5.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.5.2rc2/doc/sphinxext/math_symbol_table.py"
              data-name="v1.5.2rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.5.2rc2">
                v1.5.2rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.5.2rc1/doc/sphinxext/math_symbol_table.py"
              data-name="v1.5.2rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.5.2rc1">
                v1.5.2rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.5.1/doc/sphinxext/math_symbol_table.py"
              data-name="v1.5.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.5.1">
                v1.5.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.5.1rc1/doc/sphinxext/math_symbol_table.py"
              data-name="v1.5.1rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.5.1rc1">
                v1.5.1rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.5.0/doc/sphinxext/math_symbol_table.py"
              data-name="v1.5.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.5.0">
                v1.5.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.5.0rc3/doc/sphinxext/math_symbol_table.py"
              data-name="v1.5.0rc3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.5.0rc3">
                v1.5.0rc3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.5.0rc2/doc/sphinxext/math_symbol_table.py"
              data-name="v1.5.0rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.5.0rc2">
                v1.5.0rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.5.0rc1/doc/sphinxext/math_symbol_table.py"
              data-name="v1.5.0rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.5.0rc1">
                v1.5.0rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.4.3/doc/sphinxext/math_symbol_table.py"
              data-name="v1.4.3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.4.3">
                v1.4.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.4.3rc1/doc/sphinxext/math_symbol_table.py"
              data-name="v1.4.3rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.4.3rc1">
                v1.4.3rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.4.2/doc/sphinxext/math_symbol_table.py"
              data-name="v1.4.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.4.2">
                v1.4.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.4.1/doc/sphinxext/math_symbol_table.py"
              data-name="v1.4.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.4.1">
                v1.4.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.4.1rc1/doc/sphinxext/math_symbol_table.py"
              data-name="v1.4.1rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.4.1rc1">
                v1.4.1rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.4.0/doc/sphinxext/math_symbol_table.py"
              data-name="v1.4.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.4.0">
                v1.4.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.4.0rc4/doc/sphinxext/math_symbol_table.py"
              data-name="v1.4.0rc4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.4.0rc4">
                v1.4.0rc4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.4.0rc3/doc/sphinxext/math_symbol_table.py"
              data-name="v1.4.0rc3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.4.0rc3">
                v1.4.0rc3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.4.0rc2/doc/sphinxext/math_symbol_table.py"
              data-name="v1.4.0rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.4.0rc2">
                v1.4.0rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.4.0rc1/doc/sphinxext/math_symbol_table.py"
              data-name="v1.4.0rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.4.0rc1">
                v1.4.0rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.3.1/doc/sphinxext/math_symbol_table.py"
              data-name="v1.3.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.3.1">
                v1.3.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.3.1rc2/doc/sphinxext/math_symbol_table.py"
              data-name="v1.3.1rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.3.1rc2">
                v1.3.1rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.3.1rc1/doc/sphinxext/math_symbol_table.py"
              data-name="v1.3.1rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.3.1rc1">
                v1.3.1rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.3.0/doc/sphinxext/math_symbol_table.py"
              data-name="v1.3.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.3.0">
                v1.3.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.3.0rc5/doc/sphinxext/math_symbol_table.py"
              data-name="v1.3.0rc5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.3.0rc5">
                v1.3.0rc5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.3.0rc4/doc/sphinxext/math_symbol_table.py"
              data-name="v1.3.0rc4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.3.0rc4">
                v1.3.0rc4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.3.0rc3/doc/sphinxext/math_symbol_table.py"
              data-name="v1.3.0rc3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.3.0rc3">
                v1.3.0rc3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.3.0rc2/doc/sphinxext/math_symbol_table.py"
              data-name="v1.3.0rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.3.0rc2">
                v1.3.0rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.3.0rc1/doc/sphinxext/math_symbol_table.py"
              data-name="v1.3.0rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.3.0rc1">
                v1.3.0rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.2.1/doc/sphinxext/math_symbol_table.py"
              data-name="v1.2.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.2.1">
                v1.2.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.2.1rc1/doc/sphinxext/math_symbol_table.py"
              data-name="v1.2.1rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.2.1rc1">
                v1.2.1rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.2.0/doc/sphinxext/math_symbol_table.py"
              data-name="v1.2.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.2.0">
                v1.2.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.2.0rc3/doc/sphinxext/math_symbol_table.py"
              data-name="v1.2.0rc3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.2.0rc3">
                v1.2.0rc3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.2.0rc2/doc/sphinxext/math_symbol_table.py"
              data-name="v1.2.0rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.2.0rc2">
                v1.2.0rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.2.0rc1/doc/sphinxext/math_symbol_table.py"
              data-name="v1.2.0rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.2.0rc1">
                v1.2.0rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.1.1/doc/sphinxext/math_symbol_table.py"
              data-name="v1.1.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.1.1">
                v1.1.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.1.1-rc2/doc/sphinxext/math_symbol_table.py"
              data-name="v1.1.1-rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.1.1-rc2">
                v1.1.1-rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.1.0/doc/sphinxext/math_symbol_table.py"
              data-name="v1.1.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.1.0">
                v1.1.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.1.0-rc1/doc/sphinxext/math_symbol_table.py"
              data-name="v1.1.0-rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.1.0-rc1">
                v1.1.0-rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.0.1/doc/sphinxext/math_symbol_table.py"
              data-name="v1.0.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.0.1">
                v1.0.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v1.0.0/doc/sphinxext/math_symbol_table.py"
              data-name="v1.0.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.0.0">
                v1.0.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v0.99.0/doc/sphinxext/math_symbol_table.py"
              data-name="v0.99.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.99.0">
                v0.99.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v0.99.0.rc1/doc/sphinxext/math_symbol_table.py"
              data-name="v0.99.0.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.99.0.rc1">
                v0.99.0.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v0.98.5/doc/sphinxext/math_symbol_table.py"
              data-name="v0.98.5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.98.5">
                v0.98.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v0.98.4/doc/sphinxext/math_symbol_table.py"
              data-name="v0.98.4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.98.4">
                v0.98.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v0.98.3/doc/sphinxext/math_symbol_table.py"
              data-name="v0.98.3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.98.3">
                v0.98.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v0.98.2/doc/sphinxext/math_symbol_table.py"
              data-name="v0.98.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.98.2">
                v0.98.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v0.98.1/doc/sphinxext/math_symbol_table.py"
              data-name="v0.98.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.98.1">
                v0.98.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v0.98.0/doc/sphinxext/math_symbol_table.py"
              data-name="v0.98.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.98.0">
                v0.98.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v0.91.4/doc/sphinxext/math_symbol_table.py"
              data-name="v0.91.4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.91.4">
                v0.91.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v0.91.3/doc/sphinxext/math_symbol_table.py"
              data-name="v0.91.3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.91.3">
                v0.91.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/v0.91.2/doc/sphinxext/math_symbol_table.py"
              data-name="v0.91.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.91.2">
                v0.91.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/matplotlib/matplotlib/tree/1.3.1/doc/sphinxext/math_symbol_table.py"
              data-name="1.3.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="1.3.1">
                1.3.1
              </span>
            </a>
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

    <div class="BtnGroup float-right">
      <a href="/matplotlib/matplotlib/find/master"
            class="js-pjax-capture-input btn btn-sm BtnGroup-item"
            data-pjax
            data-hotkey="t">
        Find file
      </a>
      <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm BtnGroup-item tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
    </div>
    <div class="breadcrumb js-zeroclipboard-target">
      <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/matplotlib/matplotlib"><span>matplotlib</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a href="/matplotlib/matplotlib/tree/master/doc"><span>doc</span></a></span><span class="separator">/</span><span class="js-path-segment"><a href="/matplotlib/matplotlib/tree/master/doc/sphinxext"><span>sphinxext</span></a></span><span class="separator">/</span><strong class="final-path">math_symbol_table.py</strong>
    </div>
  </div>


  <include-fragment class="commit-tease" src="/matplotlib/matplotlib/contributors/master/doc/sphinxext/math_symbol_table.py">
    <div>
      Fetching contributors&hellip;
    </div>

    <div class="commit-tease-contributors">
      <img alt="" class="loader-loading float-left" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" />
      <span class="loader-error">Cannot retrieve contributors at this time</span>
    </div>
</include-fragment>
  <div class="file">
    <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a href="/matplotlib/matplotlib/raw/master/doc/sphinxext/math_symbol_table.py" class="btn btn-sm BtnGroup-item" id="raw-url">Raw</a>
        <a href="/matplotlib/matplotlib/blame/master/doc/sphinxext/math_symbol_table.py" class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b">Blame</a>
      <a href="/matplotlib/matplotlib/commits/master/doc/sphinxext/math_symbol_table.py" class="btn btn-sm BtnGroup-item" rel="nofollow">History</a>
    </div>


        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/matplotlib/matplotlib/edit/master/doc/sphinxext/math_symbol_table.py" class="inline-form js-update-url-with-hash" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="6rVCASFd4toGzRNu44f3e/J/uDFXKeZDDwUFKxxSfa9z226iRpQoZubVJYA43TT+NIDds/0CkKY1ImbIenJKKg==" /></div>
          <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
            aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
          </button>
</form>        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/matplotlib/matplotlib/delete/master/doc/sphinxext/math_symbol_table.py" class="inline-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="0TROPLfev07N5ic6xADzdGUzv9P3lJ0uypQxjiAJuPp8UHP/AEMwX8D1v0/ywZtXYhTRcPMHKfR820IhjZC6CA==" /></div>
          <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Fork this project and delete the file" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
          </button>
</form>  </div>

  <div class="file-info">
      160 lines (150 sloc)
      <span class="file-info-divider"></span>
    6.76 KB
  </div>
</div>

    

  <div itemprop="text" class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-c1">__future__</span> <span class="pl-k">import</span> print_function</td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line">symbols <span class="pl-k">=</span> [</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line">    [<span class="pl-s"><span class="pl-pds">&quot;</span>Lower-case Greek<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line">     <span class="pl-c1">5</span>,</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line">     <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;&quot;&quot;</span><span class="pl-cce">\a</span>lpha <span class="pl-c1">\b</span>eta <span class="pl-cce">\g</span>amma <span class="pl-cce">\c</span>hi <span class="pl-c1">\d</span>elta <span class="pl-cce">\e</span>psilon <span class="pl-cce">\e</span>ta <span class="pl-cce">\i</span>ota <span class="pl-cce">\k</span>appa</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">         <span class="pl-cce">\l</span>ambda <span class="pl-cce">\m</span>u <span class="pl-cce">\n</span>u <span class="pl-cce">\o</span>mega <span class="pl-cce">\p</span>hi <span class="pl-cce">\p</span>i <span class="pl-cce">\p</span>si <span class="pl-cce">\r</span>ho <span class="pl-c1">\s</span>igma <span class="pl-cce">\t</span>au <span class="pl-cce">\t</span>heta</span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">         <span class="pl-cce">\u</span>psilon <span class="pl-cce">\x</span>i <span class="pl-cce">\z</span>eta <span class="pl-c1">\d</span>igamma <span class="pl-cce">\v</span>arepsilon <span class="pl-cce">\v</span>arkappa <span class="pl-cce">\v</span>arphi</span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">         <span class="pl-cce">\v</span>arpi <span class="pl-cce">\v</span>arrho <span class="pl-cce">\v</span>arsigma <span class="pl-cce">\v</span>artheta<span class="pl-pds">&quot;&quot;&quot;</span></span>],</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line">    [<span class="pl-s"><span class="pl-pds">&quot;</span>Upper-case Greek<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line">     <span class="pl-c1">6</span>,</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line">     <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;&quot;&quot;</span><span class="pl-c1">\D</span>elta <span class="pl-cce">\G</span>amma <span class="pl-cce">\L</span>ambda <span class="pl-cce">\O</span>mega <span class="pl-cce">\P</span>hi <span class="pl-cce">\P</span>i <span class="pl-cce">\P</span>si <span class="pl-c1">\S</span>igma <span class="pl-cce">\T</span>heta</span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\U</span>psilon <span class="pl-cce">\X</span>i <span class="pl-cce">\m</span>ho <span class="pl-cce">\n</span>abla<span class="pl-pds">&quot;&quot;&quot;</span></span>],</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line">    [<span class="pl-s"><span class="pl-pds">&quot;</span>Hebrew<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">     <span class="pl-c1">4</span>,</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">     <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;&quot;&quot;</span><span class="pl-cce">\a</span>leph <span class="pl-c1">\b</span>eth <span class="pl-c1">\d</span>aleth <span class="pl-cce">\g</span>imel<span class="pl-pds">&quot;&quot;&quot;</span></span>],</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line">    [<span class="pl-s"><span class="pl-pds">&quot;</span>Delimiters<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">     <span class="pl-c1">6</span>,</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">     <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;&quot;&quot;</span><span class="pl-k">|</span> <span class="pl-cce">\{</span> <span class="pl-cce">\l</span>floor / <span class="pl-cce">\U</span>parrow <span class="pl-cce">\l</span>lcorner <span class="pl-cce">\v</span>ert <span class="pl-cce">\}</span> <span class="pl-cce">\r</span>floor <span class="pl-c1">\b</span>ackslash</span></td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">         <span class="pl-cce">\u</span>parrow <span class="pl-cce">\l</span>rcorner <span class="pl-cce">\|</span> <span class="pl-cce">\l</span>angle <span class="pl-cce">\l</span>ceil <span class="pl-c1">[</span><span class="pl-c1"> </span><span class="pl-c1">\D</span><span class="pl-c1">ownarrow </span><span class="pl-cce">\u</span><span class="pl-c1">lcorner</span></span></td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line"><span class="pl-sr"><span class="pl-c1">         </span><span class="pl-cce">\V</span><span class="pl-c1">ert </span><span class="pl-cce">\r</span><span class="pl-c1">angle </span><span class="pl-cce">\r</span><span class="pl-c1">ceil </span><span class="pl-c1">]</span> <span class="pl-c1">\d</span>ownarrow <span class="pl-cce">\u</span>rcorner<span class="pl-pds">&quot;&quot;&quot;</span></span>],</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">    [<span class="pl-s"><span class="pl-pds">&quot;</span>Big symbols<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">     <span class="pl-c1">5</span>,</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">     <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;&quot;&quot;</span><span class="pl-c1">\b</span>igcap <span class="pl-c1">\b</span>igcup <span class="pl-c1">\b</span>igodot <span class="pl-c1">\b</span>igoplus <span class="pl-c1">\b</span>igotimes <span class="pl-c1">\b</span>iguplus</span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">         <span class="pl-c1">\b</span>igvee <span class="pl-c1">\b</span>igwedge <span class="pl-cce">\c</span>oprod <span class="pl-cce">\o</span>int <span class="pl-cce">\p</span>rod <span class="pl-c1">\s</span>um <span class="pl-cce">\i</span>nt<span class="pl-pds">&quot;&quot;&quot;</span></span>],</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">    [<span class="pl-s"><span class="pl-pds">&quot;</span>Standard function names<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">     <span class="pl-c1">4</span>,</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">     <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;&quot;&quot;</span><span class="pl-cce">\a</span>rccos <span class="pl-cce">\c</span>sc <span class="pl-cce">\k</span>er <span class="pl-cce">\m</span>in <span class="pl-cce">\a</span>rcsin <span class="pl-c1">\d</span>eg <span class="pl-cce">\l</span>g <span class="pl-cce">\P</span>r <span class="pl-cce">\a</span>rctan <span class="pl-c1">\d</span>et <span class="pl-cce">\l</span>im</span></td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">         <span class="pl-cce">\g</span>cd <span class="pl-cce">\l</span>n <span class="pl-c1">\s</span>up <span class="pl-cce">\c</span>ot <span class="pl-cce">\h</span>om <span class="pl-cce">\l</span>og <span class="pl-cce">\t</span>an <span class="pl-cce">\c</span>oth <span class="pl-cce">\i</span>nf <span class="pl-cce">\m</span>ax <span class="pl-cce">\t</span>anh</span></td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">         <span class="pl-c1">\s</span>ec <span class="pl-cce">\a</span>rg <span class="pl-c1">\d</span>im <span class="pl-cce">\l</span>iminf <span class="pl-c1">\s</span>in <span class="pl-cce">\c</span>os <span class="pl-cce">\e</span>xp <span class="pl-cce">\l</span>imsup <span class="pl-c1">\s</span>inh <span class="pl-cce">\c</span>osh<span class="pl-pds">&quot;&quot;&quot;</span></span>],</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">    [<span class="pl-s"><span class="pl-pds">&quot;</span>Binary operation and relation symbols<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">     <span class="pl-c1">3</span>,</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">     <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;&quot;&quot;</span><span class="pl-cce">\a</span>st <span class="pl-cce">\p</span>m <span class="pl-c1">\s</span>lash <span class="pl-cce">\c</span>ap <span class="pl-c1">\s</span>tar <span class="pl-cce">\m</span>p <span class="pl-cce">\c</span>up <span class="pl-cce">\c</span>dot <span class="pl-cce">\u</span>plus</span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\t</span>riangleleft <span class="pl-cce">\c</span>irc <span class="pl-cce">\o</span>dot <span class="pl-c1">\s</span>qcap <span class="pl-cce">\t</span>riangleright <span class="pl-c1">\b</span>ullet <span class="pl-cce">\o</span>minus</span></td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-c1">\s</span>qcup <span class="pl-c1">\b</span>igcirc <span class="pl-cce">\o</span>plus <span class="pl-c1">\w</span>edge <span class="pl-c1">\d</span>iamond <span class="pl-cce">\o</span>slash <span class="pl-cce">\v</span>ee</span></td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-c1">\b</span>igtriangledown <span class="pl-cce">\t</span>imes <span class="pl-cce">\o</span>times <span class="pl-c1">\d</span>ag <span class="pl-c1">\b</span>igtriangleup <span class="pl-c1">\d</span>iv <span class="pl-c1">\w</span>r</span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-c1">\d</span>dag <span class="pl-c1">\b</span>arwedge <span class="pl-cce">\v</span>eebar <span class="pl-c1">\b</span>oxplus <span class="pl-cce">\c</span>urlywedge <span class="pl-cce">\c</span>urlyvee <span class="pl-c1">\b</span>oxminus</span></td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\C</span>ap <span class="pl-cce">\C</span>up <span class="pl-c1">\b</span>oxtimes <span class="pl-c1">\b</span>ot <span class="pl-cce">\t</span>op <span class="pl-c1">\d</span>otplus <span class="pl-c1">\b</span>oxdot <span class="pl-cce">\i</span>ntercal</span></td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\r</span>ightthreetimes <span class="pl-c1">\d</span>ivideontimes <span class="pl-cce">\l</span>eftthreetimes <span class="pl-cce">\e</span>quiv <span class="pl-cce">\l</span>eq <span class="pl-cce">\g</span>eq</span></td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\p</span>erp <span class="pl-cce">\c</span>ong <span class="pl-cce">\p</span>rec <span class="pl-c1">\s</span>ucc <span class="pl-cce">\m</span>id <span class="pl-cce">\n</span>eq <span class="pl-cce">\p</span>receq <span class="pl-c1">\s</span>ucceq <span class="pl-cce">\p</span>arallel <span class="pl-c1">\s</span>im</span></td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\l</span>l <span class="pl-cce">\g</span>g <span class="pl-c1">\b</span>owtie <span class="pl-c1">\s</span>imeq <span class="pl-c1">\s</span>ubset <span class="pl-c1">\s</span>upset <span class="pl-cce">\J</span>oin <span class="pl-cce">\a</span>pprox <span class="pl-c1">\s</span>ubseteq</span></td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-c1">\s</span>upseteq <span class="pl-cce">\l</span>times <span class="pl-cce">\a</span>symp <span class="pl-c1">\s</span>qsubset <span class="pl-c1">\s</span>qsupset <span class="pl-cce">\r</span>times <span class="pl-c1">\d</span>oteq</span></td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-c1">\s</span>qsubseteq <span class="pl-c1">\s</span>qsupseteq <span class="pl-c1">\s</span>mile <span class="pl-cce">\p</span>ropto <span class="pl-c1">\d</span>ashv <span class="pl-cce">\v</span>dash <span class="pl-cce">\f</span>rown</span></td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\m</span>odels <span class="pl-cce">\i</span>n <span class="pl-cce">\n</span>i <span class="pl-cce">\n</span>otin <span class="pl-cce">\a</span>pproxeq <span class="pl-cce">\l</span>eqq <span class="pl-cce">\g</span>eqq <span class="pl-cce">\l</span>essgtr <span class="pl-cce">\l</span>eqslant</span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\g</span>eqslant <span class="pl-cce">\l</span>esseqgtr <span class="pl-c1">\b</span>acksim <span class="pl-cce">\l</span>essapprox <span class="pl-cce">\g</span>trapprox <span class="pl-cce">\l</span>esseqqgtr</span></td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-c1">\b</span>acksimeq <span class="pl-cce">\l</span>ll <span class="pl-cce">\g</span>gg <span class="pl-cce">\g</span>treqqless <span class="pl-cce">\t</span>riangleq <span class="pl-cce">\l</span>essdot <span class="pl-cce">\g</span>trdot</span></td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\g</span>treqless <span class="pl-cce">\c</span>irceq <span class="pl-cce">\l</span>esssim <span class="pl-cce">\g</span>trsim <span class="pl-cce">\g</span>trless <span class="pl-c1">\b</span>umpeq <span class="pl-cce">\e</span>qslantless</span></td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\e</span>qslantgtr <span class="pl-c1">\b</span>ackepsilon <span class="pl-c1">\B</span>umpeq <span class="pl-cce">\p</span>recsim <span class="pl-c1">\s</span>uccsim <span class="pl-c1">\b</span>etween</span></td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-c1">\d</span>oteqdot <span class="pl-cce">\p</span>recapprox <span class="pl-c1">\s</span>uccapprox <span class="pl-cce">\p</span>itchfork <span class="pl-c1">\S</span>ubset <span class="pl-c1">\S</span>upset</span></td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\f</span>allingdotseq <span class="pl-c1">\s</span>ubseteqq <span class="pl-c1">\s</span>upseteqq <span class="pl-cce">\r</span>isingdotseq <span class="pl-c1">\s</span>qsubset</span></td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-c1">\s</span>qsupset <span class="pl-cce">\v</span>arpropto <span class="pl-cce">\p</span>reccurlyeq <span class="pl-c1">\s</span>ucccurlyeq <span class="pl-cce">\V</span>dash <span class="pl-cce">\t</span>herefore</span></td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\c</span>urlyeqprec <span class="pl-cce">\c</span>urlyeqsucc <span class="pl-cce">\v</span>Dash <span class="pl-c1">\b</span>ecause <span class="pl-c1">\b</span>lacktriangleleft</span></td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-c1">\b</span>lacktriangleright <span class="pl-cce">\V</span>vdash <span class="pl-cce">\e</span>qcirc <span class="pl-cce">\t</span>rianglelefteq</span></td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\t</span>rianglerighteq <span class="pl-cce">\n</span>eq <span class="pl-cce">\v</span>artriangleleft <span class="pl-cce">\v</span>artriangleright <span class="pl-cce">\n</span>cong</span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\n</span>leq <span class="pl-cce">\n</span>geq <span class="pl-cce">\n</span>subseteq <span class="pl-cce">\n</span>mid <span class="pl-cce">\n</span>supseteq <span class="pl-cce">\n</span>parallel <span class="pl-cce">\n</span>less <span class="pl-cce">\n</span>gtr</span></td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\n</span>prec <span class="pl-cce">\n</span>succ <span class="pl-c1">\s</span>ubsetneq <span class="pl-cce">\n</span>sim <span class="pl-c1">\s</span>upsetneq <span class="pl-cce">\n</span>VDash <span class="pl-cce">\p</span>recnapprox</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-c1">\s</span>uccnapprox <span class="pl-c1">\s</span>ubsetneqq <span class="pl-cce">\n</span>vDash <span class="pl-cce">\p</span>recnsim <span class="pl-c1">\s</span>uccnsim <span class="pl-c1">\s</span>upsetneqq</span></td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\n</span>vdash <span class="pl-cce">\l</span>napprox <span class="pl-cce">\g</span>napprox <span class="pl-cce">\n</span>triangleleft <span class="pl-cce">\n</span>trianglelefteq</span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\l</span>neqq <span class="pl-cce">\g</span>neqq <span class="pl-cce">\n</span>triangleright <span class="pl-cce">\l</span>nsim <span class="pl-cce">\g</span>nsim <span class="pl-cce">\n</span>trianglerighteq</span></td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\c</span>oloneq <span class="pl-cce">\e</span>qsim <span class="pl-cce">\n</span>equiv <span class="pl-cce">\n</span>approx <span class="pl-cce">\n</span>supset <span class="pl-c1">\d</span>oublebarwedge <span class="pl-cce">\n</span>Vdash</span></td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-c1">\D</span>oteq <span class="pl-cce">\n</span>subset <span class="pl-cce">\e</span>qcolon <span class="pl-cce">\n</span>e</span></td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-pds">&quot;&quot;&quot;</span></span>],</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">    [<span class="pl-s"><span class="pl-pds">&quot;</span>Arrow symbols<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">     <span class="pl-c1">2</span>,</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">     <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;&quot;&quot;</span><span class="pl-cce">\l</span>eftarrow <span class="pl-cce">\l</span>ongleftarrow <span class="pl-cce">\u</span>parrow <span class="pl-cce">\L</span>eftarrow <span class="pl-cce">\L</span>ongleftarrow</span></td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\U</span>parrow <span class="pl-cce">\r</span>ightarrow <span class="pl-cce">\l</span>ongrightarrow <span class="pl-c1">\d</span>ownarrow <span class="pl-cce">\R</span>ightarrow</span></td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\L</span>ongrightarrow <span class="pl-c1">\D</span>ownarrow <span class="pl-cce">\l</span>eftrightarrow <span class="pl-cce">\u</span>pdownarrow</span></td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\l</span>ongleftrightarrow <span class="pl-cce">\u</span>pdownarrow <span class="pl-cce">\L</span>eftrightarrow</span></td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\L</span>ongleftrightarrow <span class="pl-cce">\U</span>pdownarrow <span class="pl-cce">\m</span>apsto <span class="pl-cce">\l</span>ongmapsto <span class="pl-cce">\n</span>earrow</span></td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\h</span>ookleftarrow <span class="pl-cce">\h</span>ookrightarrow <span class="pl-c1">\s</span>earrow <span class="pl-cce">\l</span>eftharpoonup</span></td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\r</span>ightharpoonup <span class="pl-c1">\s</span>warrow <span class="pl-cce">\l</span>eftharpoondown <span class="pl-cce">\r</span>ightharpoondown</span></td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\n</span>warrow <span class="pl-cce">\r</span>ightleftharpoons <span class="pl-cce">\l</span>eadsto <span class="pl-c1">\d</span>ashrightarrow</span></td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-c1">\d</span>ashleftarrow <span class="pl-cce">\l</span>eftleftarrows <span class="pl-cce">\l</span>eftrightarrows <span class="pl-cce">\L</span>leftarrow</span></td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\R</span>rightarrow <span class="pl-cce">\t</span>woheadleftarrow <span class="pl-cce">\l</span>eftarrowtail <span class="pl-cce">\l</span>ooparrowleft</span></td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\l</span>eftrightharpoons <span class="pl-cce">\c</span>urvearrowleft <span class="pl-cce">\c</span>irclearrowleft <span class="pl-cce">\L</span>sh</span></td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\u</span>puparrows <span class="pl-cce">\u</span>pharpoonleft <span class="pl-c1">\d</span>ownharpoonleft <span class="pl-cce">\m</span>ultimap</span></td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\l</span>eftrightsquigarrow <span class="pl-cce">\r</span>ightrightarrows <span class="pl-cce">\r</span>ightleftarrows</span></td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\r</span>ightrightarrows <span class="pl-cce">\r</span>ightleftarrows <span class="pl-cce">\t</span>woheadrightarrow</span></td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\r</span>ightarrowtail <span class="pl-cce">\l</span>ooparrowright <span class="pl-cce">\r</span>ightleftharpoons</span></td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\c</span>urvearrowright <span class="pl-cce">\c</span>irclearrowright <span class="pl-cce">\R</span>sh <span class="pl-c1">\d</span>owndownarrows</span></td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\u</span>pharpoonright <span class="pl-c1">\d</span>ownharpoonright <span class="pl-cce">\r</span>ightsquigarrow <span class="pl-cce">\n</span>leftarrow</span></td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\n</span>rightarrow <span class="pl-cce">\n</span>Leftarrow <span class="pl-cce">\n</span>Rightarrow <span class="pl-cce">\n</span>leftrightarrow</span></td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\n</span>Leftrightarrow <span class="pl-cce">\t</span>o <span class="pl-c1">\S</span>warrow <span class="pl-c1">\S</span>earrow <span class="pl-cce">\N</span>warrow <span class="pl-cce">\N</span>earrow</span></td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\l</span>eftsquigarrow</span></td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-pds">&quot;&quot;&quot;</span></span>],</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">    [<span class="pl-s"><span class="pl-pds">&quot;</span>Miscellaneous symbols<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">     <span class="pl-c1">3</span>,</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">     <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;&quot;&quot;</span><span class="pl-cce">\n</span>eg <span class="pl-cce">\i</span>nfty <span class="pl-cce">\f</span>orall <span class="pl-c1">\w</span>p <span class="pl-cce">\e</span>xists <span class="pl-c1">\b</span>igstar <span class="pl-cce">\a</span>ngle <span class="pl-cce">\p</span>artial</span></td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\n</span>exists <span class="pl-cce">\m</span>easuredangle <span class="pl-cce">\e</span>th <span class="pl-cce">\e</span>mptyset <span class="pl-c1">\s</span>phericalangle <span class="pl-cce">\c</span>lubsuit</span></td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\v</span>arnothing <span class="pl-cce">\c</span>omplement <span class="pl-c1">\d</span>iamondsuit <span class="pl-cce">\i</span>math <span class="pl-cce">\F</span>inv <span class="pl-cce">\t</span>riangledown</span></td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\h</span>eartsuit <span class="pl-cce">\j</span>math <span class="pl-cce">\G</span>ame <span class="pl-c1">\s</span>padesuit <span class="pl-cce">\e</span>ll <span class="pl-cce">\h</span>bar <span class="pl-cce">\v</span>artriangle <span class="pl-cce">\c</span>dots</span></td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\h</span>slash <span class="pl-cce">\v</span>dots <span class="pl-c1">\b</span>lacksquare <span class="pl-cce">\l</span>dots <span class="pl-c1">\b</span>lacktriangle <span class="pl-c1">\d</span>dots <span class="pl-c1">\s</span>harp</span></td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\p</span>rime <span class="pl-c1">\b</span>lacktriangledown <span class="pl-cce">\I</span>m <span class="pl-cce">\f</span>lat <span class="pl-c1">\b</span>ackprime <span class="pl-cce">\R</span>e <span class="pl-cce">\n</span>atural</span></td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\c</span>ircledS <span class="pl-cce">\P</span> <span class="pl-cce">\c</span>opyright <span class="pl-c1">\s</span>s <span class="pl-cce">\c</span>ircledR <span class="pl-c1">\S</span> <span class="pl-cce">\y</span>en <span class="pl-c1">\A</span>A <span class="pl-cce">\c</span>heckmark <span class="pl-cce">\$</span></span></td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line"><span class="pl-sr">     <span class="pl-cce">\i</span>iint <span class="pl-cce">\i</span>int <span class="pl-cce">\i</span>int <span class="pl-cce">\o</span>iiint<span class="pl-pds">&quot;&quot;&quot;</span></span>]</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">]</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">run</span>(<span class="pl-smi">state_machine</span>):</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_n</span>(<span class="pl-smi">n</span>, <span class="pl-smi">l</span>):</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">        part <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> x <span class="pl-k">in</span> l:</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">            part.append(x)</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">len</span>(part) <span class="pl-k">==</span> n:</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">yield</span> part</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">                part <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">yield</span> part</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">    lines <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> category, columns, syms <span class="pl-k">in</span> symbols:</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">        syms <span class="pl-k">=</span> <span class="pl-c1">sorted</span>(syms.split())</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">        lines.append(<span class="pl-s"><span class="pl-pds">&quot;</span>**<span class="pl-c1">%s</span>**<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> category)</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">        lines.append(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">        max_width <span class="pl-k">=</span> <span class="pl-c1">max</span>(<span class="pl-c1">map</span>(<span class="pl-c1">len</span>, syms)) <span class="pl-k">*</span> <span class="pl-c1">2</span> <span class="pl-k">+</span> <span class="pl-c1">16</span></td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">        header <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>    <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> ((<span class="pl-s"><span class="pl-pds">&#39;</span>=<span class="pl-pds">&#39;</span></span> <span class="pl-k">*</span> max_width) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>) <span class="pl-k">*</span> columns</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">format</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%%%d</span>s<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> max_width</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> chunk <span class="pl-k">in</span> get_n(<span class="pl-c1">20</span>, get_n(columns, syms)):</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">            lines.append(header)</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> part <span class="pl-k">in</span> chunk:</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">                line <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> sym <span class="pl-k">in</span> part:</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">                    line.append(<span class="pl-c1">format</span> <span class="pl-k">%</span> (<span class="pl-s"><span class="pl-pds">&quot;</span>:math:`<span class="pl-c1">%s</span>` ``<span class="pl-c1">%s</span>``<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (sym, sym)))</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">                lines.append(<span class="pl-s"><span class="pl-pds">&quot;</span>    <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span>.join(line))</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">            lines.append(header)</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">            lines.append(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">    state_machine.insert_input(lines, <span class="pl-s"><span class="pl-pds">&quot;</span>Symbol table<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> []</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">math_symbol_table_directive</span>(<span class="pl-smi">name</span>, <span class="pl-smi">arguments</span>, <span class="pl-smi">options</span>, <span class="pl-smi">content</span>, <span class="pl-smi">lineno</span>,</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">                                <span class="pl-smi">content_offset</span>, <span class="pl-smi">block_text</span>, <span class="pl-smi">state</span>, <span class="pl-smi">state_machine</span>):</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> run(state_machine)</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">setup</span>(<span class="pl-smi">app</span>):</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">    app.add_directive(</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>math_symbol_table<span class="pl-pds">&#39;</span></span>, math_symbol_table_directive,</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">False</span>, (<span class="pl-c1">0</span>, <span class="pl-c1">1</span>, <span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">    metadata <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>parallel_read_safe<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">True</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>parallel_write_safe<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">True</span>}</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> metadata</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>__main__<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Do some verification of the tables</span></td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">from</span> matplotlib <span class="pl-k">import</span> _mathtext_data</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>SYMBOLS NOT IN STIX:<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">    all_symbols <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> category, columns, syms <span class="pl-k">in</span> symbols:</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> category <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Standard Function Names<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">        syms <span class="pl-k">=</span> syms.split()</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> sym <span class="pl-k">in</span> syms:</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">len</span>(sym) <span class="pl-k">&gt;</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">                all_symbols[sym[<span class="pl-c1">1</span>:]] <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> sym[<span class="pl-c1">1</span>:] <span class="pl-k">not</span> <span class="pl-k">in</span> _mathtext_data.tex2uni:</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">print</span>(sym)</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>SYMBOLS NOT IN TABLE:<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> sym <span class="pl-k">in</span> _mathtext_data.tex2uni:</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> sym <span class="pl-k">not</span> <span class="pl-k">in</span> all_symbols:</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(sym)</td>
      </tr>
</table>

  </div>

  </div>

  <button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
  <div id="jump-to-line" style="display:none">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
      <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
      <button type="submit" class="btn">Go</button>
</form>  </div>

  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

      
<div class="container site-footer-container">
  <div class="site-footer " role="contentinfo">
    <ul class="site-footer-links float-right">
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage" class="site-footer-mark" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2017 <span title="0.21886s from unicorn-849612207-l5320">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
    You can't perform that action at this time.
  </div>


    
    <script crossorigin="anonymous" integrity="sha256-nL0D6lZGHoSriVa/d5mpd9bMih+YTHG17LLt/bo9dz8=" src="https://assets-cdn.github.com/assets/frameworks-9cbd03ea56461e84ab8956bf7799a977d6cc8a1f984c71b5ecb2edfdba3d773f.js"></script>
    
    <script async="async" crossorigin="anonymous" integrity="sha256-MpVEs6V4fIUQfgMDkQu7L2eCLO/3/J/ptXlamQDQEwI=" src="https://assets-cdn.github.com/assets/github-329544b3a5787c85107e0303910bbb2f67822ceff7fc9fe9b5795a9900d01302.js"></script>
    
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
  </div>
</div>


  </body>
</html>

